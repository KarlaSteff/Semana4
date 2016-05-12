def abrirtxt():
	archi=open('leerarchivo.txt','r')

def conteo():
	archi=open('leerarchivo.txt','r')
	linea=archi.readline()
	while linea!="":
		contador=linea.split(".")
		for i in range(len(contador)):
			palabra=len(contador[i].split(" "))
			print ("La frase: \n(" +str(linea) +")" +" \ntiene " +str(palabra) +" palabras")
			linea=archi.readline()
			archi.close()

abrirtxt()
conteo()