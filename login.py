def iniciar_sesion():
    try:
        archivo = open("iniciarSesion.txt", "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
        
        usuarios = {}
        for linea in lineas:
            nombre, password = linea.strip().split(":")
            usuarios[nombre] = password
    except Exception as e:
        print("No hay usuarios registrados. Comenzando la creación de usuario.")
        return crear_usuario()

    nombre = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    if nombre in usuarios and usuarios[nombre] == password:
        print("Sesión iniciada")
        print("Bienvenido al programa")
        menu()
    else:
        print("Usuario no existente. Crea un usuario.")
        crear_usuario()

def crear_usuario():
    try:
        archivo = open("iniciarSesion.txt", "r+", encoding="utf-8")
        lineas = archivo.readlines()
        usuarios = {}
        
        for linea in lineas:
            nombre, password = linea.strip().split(":")
            usuarios[nombre] = password
    except Exception as e:
        archivo = open("iniciarSesion.txt", "w+", encoding="utf-8")
        usuarios = {}

    while True:
        nombre = input("Ingrese un nuevo nombre de usuario: ")
        if nombre in usuarios:
            print("Usuario ya existente, vuelva a intentar.")
        else:
            break
    
    password = input("Ingrese una nueva contraseña: ")
    archivo.write(f"{nombre}:{password}\n")
    archivo.close()
    
    print("Usuario creado satisfactoriamente.")
    iniciar_sesion()

def salir ():
    print("Fin del programa")
    exit()
    
def menu():
    opcion = input("Que quieres hacer? (1) Iniciar sesion (2) Crear usuario (3) Salir: ")
    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        crear_usuario()
    elif opcion == "3":
        salir()
    else:
        print("Opcion no valida.")
        menu()

menu()
