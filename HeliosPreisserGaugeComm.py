import serial
import time
import glob

class Gauge():
    """
    Class for controlling and reading the Helios Preisser
    Digimet 1722-502 digital dial indicator
    along with the 1998-720 Digimatic data to USB cable.

    Some troubleshooting of USB protocol here
    https://stackoverflow.com/questions/66675302/failing-to-communicate-with-digital-dial-indicator-via-usb-serial-python-library/66676815#66676815

    to read with press button, set dsrdtr=True
    
    """

    def __init__(self, port = '', debug=False):

        self.port = port
        self.baudrate = 4800
        self.parity=serial.PARITY_EVEN
        self.bytesize=serial.SEVENBITS
        self.stopbits=serial.STOPBITS_TWO
        self.debug=debug
        self.ser = serial.Serial()
        self.openSerialPort()
        self.initRead()
        #self.readGauge()

    def setVerbose(self, debug=True):
        self.debug=debug
        
    def openSerialPort(self):
        self.ser.port = self.port
        self.ser.baudrate = self.baudrate
        self.ser.parity=self.parity
        self.ser.bytesize=self.bytesize
        self.ser.stopbits=self.stopbits
        try:
            self.ser.open()
        except(serial.SerialException):
            print("Failed to open serial port {}".format(self.ser.port))
        
    def closeSerialPort(self):
        self.ser.close()

    def initRead(self):
        self.ser.dtr=False
        self.ser.rts=False

    def readGauge(self):
        """
        """
        self.ser.rts=True
        time.sleep(0.2)
        self.ser.rts=False
        time.sleep(0.1)

        resp = str(self.ser.read(self.ser.inWaiting()))
        if self.debug: print(resp)
        ssign = resp[2]
        smag = resp[3:9]
        try:
            mag = float(smag)
        except:
            mag = float('nan')
        if ssign == '+':
            pos = mag
        elif ssign == '-':
            pos = -mag
        if self.debug: print("POSITION: %f"%pos)
        
        return pos

