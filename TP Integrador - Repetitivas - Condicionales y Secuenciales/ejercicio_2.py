#Ingreso a Campus

#Credenciales validas para ingresar al campus
usuario_correcto = "alumno"
clave_correcta = "python123"

#Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
print("Ingrese sus credenciales")
usuario = input("Ingrese su usuario: ")
while not usuario == usuario_correcto:
    print("Error! El usuario no existe.")
    usuario = input("Ingrese su usuario: ")

intentos = 3
acceso = False

while intentos > 0:
    clave = input(f"Ingrese su clave: (intentos restantes: {intentos}): ")
    print("-" * 30)

    #Si la clave coincide, se le da acceso a la cuenta
    if clave == clave_correcta:
        acceso = True
        break
    else:
        intentos -= 1
        if intentos > 0:
            print("Contraseña incorrecta, intente devuelta")

#Si el acceso es True, entra al campus
if acceso:
    print("Bienvenido!")

#Bloqueo la cuenta si supera los 3 intentos 
else:
    print("CUENTA BLOQUEADA!")
    print("-" * 30)
    exit()

print("-" * 30)
print("1 - Ver estado de inscripción")
print("2 - Cambiar clave")
print("3 - Mostrar mensaje motivacional")
print("4 - Salir")
print("-" * 30)

opcion = input("Seleccione una opción: ")

#Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
while not opcion.isdigit(): 
    print("Ingrese un número válido")
    opcion = input("Ingrese opción: ")
while int(opcion) < 1 or int(opcion) > 4:
    print("Opción fuera de rango")
    opcion = input("Ingrese opción: ")

while int(opcion) != 4:
    
    #Ver el estado 
    if int(opcion) == 1:
        print("-" * 30)
        print("Su estado es 'Inscripto'")

    #Cambio de clave
    elif int(opcion) == 2:
        print("-" *30)
        print("Cambie su clave")
        clave_nueva = input("Ingrese su nueva clave (mínimo de 6 caracteres): ")
        if  len(clave_nueva) >= 6:
            confirmacion = input("Confirme su nueva contraseña: ")
            if clave_nueva == confirmacion:
                clave_correcta = clave_nueva
                print("Contraseña cambiada correctamente!")
            else:
                print("Error! las claves no coinciden, no se realizaron cambios")
        else:
            print("Error! mínimo de 6 caracteres, no se realizaron cambios")

    #Frase motivacional
    elif int(opcion) == 3: 
        print("Vamos que se puede!")


    print("-" * 30)
    print("1 - Ver estado de inscripción")
    print("2 - Cambiar clave")
    print("3 - Mostrar mensaje motivacional")
    print("4 - Salir")
    print("-" * 30)

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit(): 
        print("Ingrese un número válido")
        opcion = input("Ingrese opción: ")
    while int(opcion) < 1 or int(opcion) > 4:
        print("Opción fuera de rango")
        opcion = input("Ingrese opción: ")

print("Saliendo del sistema!")