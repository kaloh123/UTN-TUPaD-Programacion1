#Arena del gladiador

print("--- Bienvenido a la arena ---")
nombre_gladiador = input("Ingrese el nombre del gladiador: ")

while not nombre_gladiador.isalpha():
    print("Nombre no valido, solo se permiten letras")
    nombre_gladiador = input("Ingrese el nombre del gladiador: ")

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
regeneracion_pocion = 30 #nueva variable para la cantidad de HP que curan las pociones
danio_base_ataque_pesado = 15
danio_base_ataque_rafaga = 5 #nueva variable para un uso más práctico de los valores
danio_base_enemigo = 12 
turno_gladiador = True


#Mientras la vida de ambos combatientes sea mayor a 0, el bucle continua
while vida_gladiador > 0 and vida_enemigo > 0:

    if turno_gladiador:
        print(f" --- TURNO DE {nombre_gladiador.upper()} ---")
        print(f"""
    Vida del gladiador: {vida_gladiador}
    Vida del enemigo: {vida_enemigo}
    Pociones de vida: {pociones_vida}

    --- MENÚ --- 
    1 - Ataque pesado
    2 - Ráfaga veloz
    3 - Curar
    """)
        
        opcion_menu = input("Seleccione su opción: ")
        
        #Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
        while not opcion_menu.isdigit():
            print("Error! Solo se admite números")
            opcion_menu = input("Seleccione su opción: ")
        while int(opcion_menu) < 1 or int(opcion_menu) > 3:
            print("Opción fuera de rango")
            opcion_menu = input("Seleccione su opción: ")

        if int(opcion_menu) == 1:
            
            #Golpe crítico
            if vida_enemigo < 20:
                golpe_critico = float(danio_base_ataque_pesado * 1.5)
                vida_enemigo -= golpe_critico
                print(f"Realizaste un golpe crítico! El enemigo recibe {golpe_critico} puntos de daño!")
            #Golpe pesado
            else:   
                vida_enemigo -= danio_base_ataque_pesado
                print(f"Realizaste un ataque pesado! El enemigo recibe {danio_base_ataque_pesado} puntos de daño")

        #Ráfaga de golpes
        if int(opcion_menu) == 2:
            print("Inicias una ráfaga de golpes!")
            for i in range (1, 4):
                vida_enemigo -= danio_base_ataque_rafaga 
                print(f"> Golpe conectado por {danio_base_ataque_rafaga} de daño")

        #Curación
        if int(opcion_menu) == 3:
            if pociones_vida > 0:
                pociones_vida -= 1  
                vida_gladiador += 30
                print("Te curaste +30 HP")
                print(f"Tu salud: {vida_gladiador}")
            else:
                print("No te quedan pociones!")

        #Se termina el turno del gladiador
        turno_gladiador = False

    #Turno del enemigo
    else: 
        if vida_enemigo > 0:
            print("--- TURNO DEL ENEMIGO ---")
            vida_gladiador -= danio_base_enemigo
            print(f"El enemigo te atacó! Recibiste {danio_base_enemigo} puntos de daño")

        #Vuelve a ser turno del gladiador después de que el enemigo haya jugado
        turno_gladiador = True

#Si la vida de alguno de los luchadores llega a 0, acá se verifica quién ganó
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador.upper()} ganó la batalla")
else:
    print("DERROTA. Perdiste la batalla")
