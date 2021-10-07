import HeliosPreisserGaugeComm  as hp
import datetime
import glob
import time
import sys
#from pylab import *

print('### Reading open ports.')
try:
    ports = glob.glob('/dev/tty.usb*')
    #ports = sort(ports)
except:
    print("Failed to find /dev/tty.usb* ports")
    sys.exit()

Ndevices = len(ports)
print("Found %d connected USB devices"%len(ports))
if Ndevices == 0:
    print("Failed to find any connected /dev/tty.usb* ports. Connect a device or change the name of the searched device")
    sys.exit()
    
print('### Initializing dial gauges.')
if Ndevices >= 1:
    s0 = hp.Gauge(port = ports[0])  # arriere droit
if Ndevices >= 2:
    s1 = hp.Gauge(port = ports[1])  # arriere gauche
if Ndevices >= 3: 
    s2 = hp.Gauge(port = ports[2])  # avant gauche
if Ndevices >= 4:
    s3 = hp.Gauge(port = ports[3])  # avant droit
interval = 0.8   # interval in seconds between reads
totalDuration= 600 # total observation duration in seconds
filePrefix = 'dialData' # output filename header
now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
fileName = "%s_%s.txt"%(filePrefix,now)
print('### Opening file: %s'%fileName)
f = open(fileName,'w')
f.write('#   \n')
f.write('#   \n')
f.write('# local time, dial position [mm] \n')
tstart = datetime.datetime.now()
dial1,dial2,dial3,dial4=[0,0,0,0]
observe=True
duration = 0
while((observe == True) & (duration <= totalDuration)) :
    try:
        tnow = datetime.datetime.now()
        duration = (tnow-tstart).seconds
        dial1 = s0.readGauge()
        dial2 = 0# s1.readGauge()
        dial3 = 0 #s2.readGauge()
        dial4 = 0 #s3.readGauge()
        f.write('%s, %4.2f, %4.2f,%4.2f, %4.2f \n'%(tnow, dial1, dial2, dial3, dial4))
        f.flush()
        print(tnow, dial3, dial4, dial1, dial2)
        time.sleep(interval)
    except KeyboardInterrupt:
        print("stop requested")
        print('### Closing file: %s'%fileName)
        observe = False
        f.close()
    except Exception:
        print('Error')
        continue
       
