#Escape room: La bóveda

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
spam_forzar_cerradura = 0

nombre_agente = input("Ingrese su nombre: ")

#Verifico que se ingrese correctamente el nombre (sin números ni caracteres especiales)
while not nombre_agente.isalpha():
    print("Error!")
    print("El nombre no debe contener números")
    nombre_agente = input("Ingrese su nombre: ")

#Uso un bucle infinito y salgo del mismo con los breaks de los if siguientes que son las condiciones para ganar o perder
while True:

    print("-" * 30)
    print(f"Agente: {nombre_agente.upper()}")
    print(f"Energía: {energia} | Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas} de 3")
    print("-" * 30)

    #Si el agente ya abrió las 3 cerraduras, el sistema se cierra acá
    if cerraduras_abiertas == 3:
        print("Felicidades! Abriste las 3 cerraduras")
        print("Ganaste!")
        break

    #Si la energia o el tiempo llega a 0 el agente pierde y el sistema se cierra acá
    if energia <= 0 or tiempo <= 0:
        print("Te quedaste sin energia o tiempo y perdiste el juego")
        print("Derrota por falta de recursos!")
        break
    
    #Si suena la alarma y el tiempo es menor a 3 y no se abrió antes la bóveda, el agente pierde por bloqueo y el sistema se cierra acá
    if alarma and tiempo <= 3: 
        print("El sistema se bloqueó! Se selló la bóveda")
        print("Derrota por bloqueo!")
        break

    #Panel de opciones
    #Le agregué una opción extra para rendirse en caso de no querer jugar más
    print("-" * 30)
    print("""
    1 - Forzar cerradura
    2 - Hackear panel
    3 - Descansar
    4 - Rendirse
    """)
    print("-" * 30)

    accion_menu = input("Seleccione una acción: ")
    print("-" * 30)

    #Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
    while not accion_menu.isdigit():
        print("Ingrese un número valido")
        accion_menu = input("Seleccione una acción: ")
    while int(accion_menu) < 1 or int(accion_menu) > 4:
        print("Opción fuera de rango")
        accion_menu = input("Seleccione una acción: ")

    #Acción forzar cerradura
    if int(accion_menu) == 1:
        spam_forzar_cerradura += 1
        energia -= 20
        tiempo -= 2

        #Si fuerza la cerradura 3 veces seguidas se activa la alarma
        if spam_forzar_cerradura == 3:
            print("Demasiados intentos! la cerradura se trabó y sonó la alarma")
            alarma = True
        else:
            if energia < 40:

                print("Riesgo de alarma")
                print("""Elecciones
                    1, 2 o 3
                    """)
                
                #Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
                seleccion_num = input("Seleccione un número: ")
                while not seleccion_num.isdigit():
                    print("Ingrese un número válido")
                    seleccion_num = input("Seleccione un número: ")
                while int(seleccion_num) < 1 or int(seleccion_num) > 3:
                    print("Selección fuera de rango")
                    seleccion_num = input("Seleccione un número: ")
                
                if int(seleccion_num) == 3:
                    print("Perdiste, la alarma sonó")
                    alarma = True
                else:
                    print("Te salvaste!")
                    cerraduras_abiertas += 1
                    print(f"Cerradura abierta! vas {cerraduras_abiertas} cerraduras abiertas de 3")
            
            if not alarma:
                cerraduras_abiertas += 1
                print(f"Cerradura abierta! vas {cerraduras_abiertas} cerraduras abiertas de 3")
    
    #Acción hackear panel
    if int(accion_menu) == 2:
        spam_forzar_cerradura = 0
        energia -= 10
        tiempo -= 3

        print("--- HACKEANDO PANEL ---")

        for i in range(1, 5):
            print(f"Hackeando... paso {i} de 4")
            codigo_parcial += "A"

        print(f"Progreso del código: {codigo_parcial}")

        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            print("Código descubierto! Abriste una cerradura!")
            codigo_parcial = ""

    #Acción descanso
    if int(accion_menu) == 3:
        spam_forzar_cerradura = 0
        tiempo -= 1
        print("Descansando...")
        recuperacion = 15

        if alarma:
            print("Es complicado descansar con el ruido de la alarma! Descansás mal")
            recuperacion -= 10
        
        energia += recuperacion

        if energia > 100:
            energia = 100

        print(f"Energia actual: {energia}")

    #Acción rendirse
    if int(accion_menu) == 4:
        print("Te rendiste")
        break

