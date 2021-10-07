# DIGI-MET
A library to communicate with DIGI-MET digital dial indicator via USB protocol. Contact me (dbarkats@gmail.com) for any questions/details

Librairie de Comparateurs  Numeriques DIGI-MET avec lecteur par USB.
ILL DAI: 84604

Hardware:
 - Comparateur digital DIGI-MET, course 12,5 mm, rés.: 10 μm, Ø 58mm, reference: 1722502
 - Cable de liaison pour interface USB pour DIGI-MET, ref: 1998720
 - acheté chez BCQ (http://www.bqc.be)

Ces comparateurs numeriques ont été utilisé pour mesurer l’alignement du systeme rail chariot apres la nouvelle installation de D11 et aussi par Germain Sounier pour mesurer la deformé des rails du pont radial au dessus du reacteur.

Le logiciel de lecture automatique des comparateurs a ete developpé par moi-meme en python.  J’ai fait fonctionner ce logiciel a partir de mon mac et Germain sur des ordi sous Linux (preté par le SI).

Ce repo contient les elements suivants:
 - le manuel: Manuel_Helios_Preisser_1722-502_electronic_dial_indicator.pdf
 - la librairie python de communication avec les comparateurs: HeliosPreisserGaugeComm.py
 - Une routine d’acquisition des comparateurs: run_dials.py
 - Un script bash pour des acquisitions plus longue: run_dials.sh

Comment ca marche ?

 1/ les comparateurs fonctionnent avec une pile interne. Des qu’on les bougent, ils s’allument. Sinon, la pile est a changer
   
 2/ Brancher le cable entre le comparateur et le port USB de  l’ordinateur de controle. Si vous voulez mettre l’ordi de controle plus loin, la boite contient des rallonges USB de 2metres. Si vous voulez controller plus qu’un seul comparateur, la boite contient aussiun HUB USB. Branchez vos comparateurs dans le HUB et le HUB dans l’ordinateur de controle.
 
 3/ Si 1 ou plusieurs comparateurs sont connecté, la routine d’acquisition peut etre demarré sans autre parametrage en lancant depuis la commande linux: python3 run_dials.py. L’acquisition doit etre lancé dans le meme repertoire que les librairies.
 
 4/ L’acquisition imprime un log a l’ecran et sauvegarde les valeurs des comparateurs dans un fichier nommé: dialData_YYYYMMDD_HHMMSS.txt (ie dialData_20211007_103602.txt). Le resultats est stocké dans une fichier texte, 1 ligne par mesure avec l’heure ie
 
 	local time, dial position [mm] 
	2021-10-07 10:33:41.806556, 0.00, 0.00,0.00, 0.00 
	2021-10-07 10:33:42.916625, 0.00, 0.00,0.00, 0.00

  5/ Parametres d’acquisition:
 - Nombre de comparateurs. run_dials.py detecte automatiquement le nombre de comparateur a lire. Si le nombre de comparateur est superieur a 1, il faut changer les lignes 50, 51, 52 pour lire ou laisser a zero les valeurs des 2ieme, 3ieme, et 4ieme comparateurs.
 - Interval entre chaque mesures: ligne 31. variable “interval”.  pour controller le temps entre chaque mesures des comparteurs. La valeur par defaut est de 0.8secondes. C’est le plus court possible. On peut l’augmenter pour ne mesurer que toutes les 5s  par exemple en changeant cette ligne (interval = 5)
 - Durée total de l’acquisition: ligne 32. Variable “totalDuration” pour controller la durée totale d’une acquisition (1 fichier). La valeure par defaut est de 600s ( 10mn).
 - Nom du fichier. Ligne: 33. Variable “filePrefix”. On peut changer le prefix du fichier a sauvegarder.

 6/ Acquisition continu. Pour faire des acquisition plus longue qu’1 seule fichier ( par exemple, une acquisition de plusieurs heures. On a une second routine d’acquisition  qui va automatiquement lancer le premier script d’acquisition  jusqu’a ce qu’on l’arrete manuellement.  Si c’est ce mode de fonctionnement qui vous interesse. Lancer simplement a la commande: run_dials.sh et celui ci va lancer automatiquement l’acquisition (python3 run_dials.py) et continuera de le relancer jusqu’a ce que vous l’arretiez manuellement (2 fois control C).
