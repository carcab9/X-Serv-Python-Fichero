#!/usr/bin/python

fich = open("/etc/passwd", "r")
lineas = fich.readlines()

for linea in lineas:
	login = linea[:linea.find(':')]
	shell = linea[linea.rfind(':')+1:]
	print("user:",login, "Shell:",shell)

print("Número de lienas:", len(lineas))
fich.close()
