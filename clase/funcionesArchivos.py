#r es para lectura
#r+ es para lectura y añadir (en caso de no existir el archivo genera error)
#w es para escritura
#w+ es para escritura y lectura (en caso de no existir el archivo lo crea)
#a es para añadir  en caso de existir el archivo no hace nada, en caso de no existir lo crea vacio
lista_nombres = ["diego", "jorge", "Laura", "Ana"]
try:
    archivo = open("archivo1.txt", "w+",encoding="utf-8")
    for i in lista_nombres:
      archivo.write(i + "\n")
    archivo.write("escritura desde python")
    print (archivo.read())
except Exception as e:
    print("Error: ", e)
finally:
    archivo.close()
    print("Archivo cerrado")
    
#que quieres hacer con el archivo, iniciar sesion o crear un usuario