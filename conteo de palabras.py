def main():
	print ("EJERCICIO CONTADOR DE PALABRAS")
	frase= str(input("Ingrese la frase: "))
	contador = 0
	cadena = len(frase)
	for i in range(0, cadena ):
		if frase[i] == " ":
 			contador= contador +1    
	print (contador + 1)
main() 