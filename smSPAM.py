#-*- coding:utf-8 -*-
# Modo de uso:
# [SixP4ck3r@fedora]$ sudo python smSPAM.py nums.txt
#
import random,time,serial, sys, os
numerosTXT =  sys.argv[1]
msg = 'Hola como estas' # Aqui el contenido del msg
menuTxt = open(numerosTXT, 'r' )  
lineas = menuTxt.readlines()
print
print len(lineas),"numeros encontrados en",numerosTXT
numero = ''
print "====================================="  
for numero in lineas:
	print "Enviando msg a",numero
	preSEND = str("echo "+str(msg)+">/tmp/sms.txt")
	os.system(preSEND)
	ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
	ser.write('ATZ\r')
	time.sleep(1)
	ser.write('AT+CMGF=1\r')
	time.sleep(1)
	ser.write('AT+CMGS='+numero+'\r')
	time.sleep(1)
	file = open("/tmp/sms.txt")
	while 1:
    		line = file.readline()
    		if not line:
      			break
   		pass
   		ser.write(line)
	ser.write(chr(26))
	line = ser.readline()
	#print line
	ser.close()
	time.sleep(5)
	print "Enviado con exito!" 
print "Todos enviados con exito!!!"
