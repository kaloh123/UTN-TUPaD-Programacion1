#Agenda de turnos

print("Agenda de turnos")
nombre_operador = input("Ingrese su nombre: ")

#turnos lunes
lunes1 = ""
lunes2 = ""
lunes3 = "PEDRO"
lunes4 = ""
#turnos martes
martes1 = "JULIETA"
martes2 = "MARCELO"
martes3 = ""
#Los separo así ya que no se pueden usar listas hago una variable para cada turno

#Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
while not nombre_operador.isalpha():
    print("Error!")
    nombre_operador = input("Ingrese su nombre: ")

#Menú de opciones
print("-" * 30)
print("""
1 - Reservar turno
2 - Cancelar turno (por nombre)
3 - Ver agenda del dia
4 - Ver resumen general
5 - Cerrar sistema
""")
print("-" * 30)

opcion_menu = input("Seleccione una opción: ")
print("-" * 30)

#Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
while not opcion_menu.isdigit(): 
    print("Ingrese un número válido")
    opcion_menu = input("Ingrese opción: ")
while int(opcion_menu) < 1 or int(opcion_menu) > 5:
    print("Opción fuera de rango")
    opcion_menu = input("Ingrese opción: ")

#Mientras el usuario no ingrese 5 se ejecuta el bucle
while int(opcion_menu) != 5:

    #Reservación turnos
    if int(opcion_menu) == 1:
        print("Reservación de turno")
        print("Dias disponibles:")
        print("""
        1 - Lunes
        2 - Martes
        3 - Salir
        """)

        dia_de_turno = input("Seleccione su opción: ")

        #Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
        while not dia_de_turno.isdigit(): 
            print("Ingrese un número válido")
            dia_de_turno = input("Ingrese opción: ")
        while int(dia_de_turno) < 1 or int(dia_de_turno) > 3:
            print("Opción fuera de rango")
            dia_de_turno = input("Ingrese opción: ")

        #Reservación dia lunes
        if int(dia_de_turno) == 1:
            if lunes1 == "":
                print("Turno lunes 1 disponible")
                nombre_paciente = input("Ingrese el nombre del paciente: ")
                lunes1 = nombre_paciente.upper()
                print(f"Turno lunes 1 reservado a paciente: {lunes1}")
            elif lunes2 == "":
                print("Turno lunes 2 disponible")
                nombre_paciente = input("Ingrese el nombre del paciente: ")
                lunes2 = nombre_paciente.upper()
                print(f"Turno lunes 2 reservado a paciente: {lunes1}")
            elif lunes3 == "":
                print("Turno lunes 3 disponible")
                nombre_paciente = input("Ingrese el nombre del paciente: ")
                lunes3 = nombre_paciente.upper()
                print(f"Turno lunes 3 reservado a paciente: {lunes3}")
            elif lunes4 == "":
                print("Turno lunes 4 disponible")
                nombre_paciente = input("Ingrese el nombre del paciente: ")
                lunes4 = nombre_paciente.upper()
                print(f"Turno lunes 4 reservado a paciente: {lunes4}")
            else:
                print("No hay turnos disponibles para el dia lunes")
        
        #Reservación dia martes
        if int(dia_de_turno) == 2:
            if martes1 == "":
                print("Turno martes 1 disponible")
                nombre_paciente = input("Ingrese el nombre del paciente: ")
                martes1 = nombre_paciente.upper()
                print(f"Turno martes 1 reservado a paciente: {martes1}")
            elif martes2 == "":
                print("Turno martes 2 disponible")
                nombre_paciente = input("Ingrese el nombre del paciente: ")
                martes2 = nombre_paciente.upper()
                print(f"Turno martes 2 reservado a paciente: {martes2}")
            elif martes3 == "":
                print("Turno martes 3 disponible")
                nombre_paciente = input("Ingrese el nombre del paciente: ")
                martes3 = nombre_paciente.upper()
                print(f"Turno martes 3 reservado a paciente: {martes3}")
            else:
                print("No hay turnos disponibles para el dia martes")

        #Si el usuario ingresa 3, sale de la opción para reservar turnos
        if int(dia_de_turno) == 3:
            pass

    #Cancelación de turnos
    elif int(opcion_menu) == 2:
        print("Cancelación de turno")
        print("Dias disponibles:")
        print("""
        1 - Lunes
        2 - Martes
        3 - Salir
        """)

        dia_de_cancelar_turno = input("Seleccione su opción: ")

        #Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
        while not dia_de_cancelar_turno.isdigit(): 
            print("Ingrese un número válido")
            dia_de_cancelar_turno = input("Ingrese opción: ")
        while int(dia_de_cancelar_turno) < 1 or int(dia_de_cancelar_turno) > 3:
            print("Opción fuera de rango")
            dia_de_cancelar_turno = input("Ingrese opción: ")
        
        #Cancela turno dia lunes
        if int(dia_de_cancelar_turno) == 1:
            nombre_paciente = input("Ingrese el nombre del paciente: ")
            nombre_paciente = nombre_paciente.upper()
            if nombre_paciente == lunes1:
                lunes1 = ""
                print("El turno lunes 1 fue cancelado")
            elif nombre_paciente == lunes2:
                lunes2 = ""
                print("El turno lunes 2 fue cancelado")
            elif nombre_paciente == lunes3:
                lunes3 = ""
                print("El turno lunes 3 fue cancelado")
            elif nombre_paciente == lunes4:
                lunes4 = ""
                print("El turno lunes 4 fue cancelado")
            else:
                print(f"El paciente {nombre_paciente} no tiene ningún turno para el dia lunes")

        #Cancela turno dia martes
        if int(dia_de_cancelar_turno) == 2:
            nombre_paciente = input("Ingrese el nombre del paciente: ")
            nombre_paciente = nombre_paciente.upper()
            if nombre_paciente == martes1:
                martes1 = ""
                print("El turno martes 1 fue cancelado")
            elif nombre_paciente == martes2:
                martes2 = ""
                print("El turno martes 2 fue cancelado")
            elif nombre_paciente == martes3:
                martes3 = ""
                print("El turno martes 3 fue cancelado")
            else:
                print(f"El paciente {nombre_paciente} no tiene ningún turno para el dia martes")
        
        #Si el usuario ingresa 3, sale de la opción para cancelar turnos
        if int(dia_de_cancelar_turno) == 3:
            pass

    #Ver la agenda del dia
    elif int(opcion_menu) == 3:
        print("Agenda del dia:")
        print("-" * 18)
        print("Lunes")
        if lunes1 != "":
            print(f"Turno 1 del lunes: {lunes1}")
        else:
            print("Turno 1 libre")
        if lunes2 != "":
            print(f"Turno 2 del lunes: {lunes2}")
        else:
            print("Turno 2 libre")
        if lunes3 != "":
            print(f"Turno 3 del lunes: {lunes3}")
        else:
            print("Turno 3 libre")
        if lunes4 != "":
            print(f"Turno 4 del lunes: {lunes4}")
        else:
            print("Turno 4 libre")      
        print("-" * 30)
        print("Martes")
        if martes1 != "":
            print(f"Turno 1 del martes: {martes1}")
        else:
            print("Turno 1 libre")
        if martes2 != "":
            print(f"Turno 2 del martes: {martes2}")
        else:
            print("Turno 2 libre")
        if martes3 != "":
            print(f"Turno 3 del martes: {martes3}")
        else:
            print("Turno 3 libre")

    #Ver un resumen general de turnos
    elif int(opcion_menu) == 4: 
        print("Resumen general")

        lunes_ocupados = 0
        if lunes1 != "":
            lunes_ocupados += 1
        if lunes2 != "":
            lunes_ocupados += 1
        if lunes3 != "":
            lunes_ocupados += 1
        if lunes4 != "":
            lunes_ocupados += 1

        lunes_disponibles = 4 - lunes_ocupados

        martes_ocupados = 0
        if martes1 != "":
            martes_ocupados += 1
        if martes2 != "":
            martes_ocupados += 1
        if martes3 != "":
            martes_ocupados += 1

        martes_disponibles = 3 - martes_ocupados

        print(f"Lunes ocupados: {lunes_ocupados} / Disponibles: {lunes_disponibles}")
        print(f"martes ocupados: {martes_ocupados} / Disponibles: {martes_disponibles}")

        #Chequeo que dia tiene más turnos ocupados 
        if lunes_ocupados > martes_ocupados:
            print("Dia con más turnos ocupados: Lunes")
        elif martes_ocupados > lunes_ocupados:
            print("Dia con más turnos ocupados: Martes")
        else:
            print("Ambos dias tienen la misma cantidad de turnos ocupados")

    print("-" * 30)
    print("""
    1 - Reservar turno
    2 - Cancelar turno (por nombre)
    3 - Ver agenda del dia
    4 - Ver resumen general
    5 - Cerrar sistema
    """)
    print("-" * 30)

    opcion_menu = input("Seleccione una opción: ")
    print("-" * 30)

    while not opcion_menu.isdigit(): 
        print("Ingrese un número válido")
        opcion_menu = input("Ingrese opción: ")
    while int(opcion_menu) < 1 or int(opcion_menu) > 5:
        print("Opción fuera de rango")
        opcion_menu = input("Ingrese opción: ")

print("Saliendo del sistema!")