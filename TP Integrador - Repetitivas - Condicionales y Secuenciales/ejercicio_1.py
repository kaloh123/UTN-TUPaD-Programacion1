#Caja de kiosco

total_sdescuento = 0
total_cdescuento = 0
ahorro_total = 0

nombre_cliente = input("Ingrese su nombre: ")

#Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
while not nombre_cliente.isalpha():
    print("Error!")
    nombre_cliente = input("Ingrese su nombre")    

#Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
cant_productos_a_comprar = input("Cantidad de productos a comprar: ")
while not cant_productos_a_comprar.isdigit() or int(cant_productos_a_comprar) <= 0:
    print("Ingrese una cantidad de productos mayor a 0")
    cant_productos_a_comprar = input("Cantidad de productos a comprar: ")

#Transformo la variable a entero para poder usarla en el for
cant_productos_a_comprar = int(cant_productos_a_comprar)
for i in range(cant_productos_a_comprar):
    
    precio = input(f"Ingrese el precio entero del prodcuto {i+1}: ")

    #Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
    while not precio.isdigit():
    
        print("Error!")
        precio = input(f"Ingrese el precio entero del producto {i+1}: ")
    
    precio = int(precio)

    print("¿Tiene descuento? S = si / N = no")
    opcion_descuento = input("Seleccione su opción: ")

    #Uso las funciones .lower() y en caso de que el usuario ingrese la opción en mayúsculas o minúsculas esta sea valida
    #Verifico que la opción ingresada por el usuario sea correcta y cumpla con los requisitos
    while opcion_descuento.lower() != "s" and opcion_descuento.lower() != "n":
        print("Opción no valida. Ingrese S o N")
        print("¿Tiene descuento? S = si / N = no")
        opcion_descuento = input("Seleccione su opción: ")
    

    if opcion_descuento.lower() == "s":
        
        descuento_producto = precio * 0.10
        ahorro_total += descuento_producto
        total_cdescuento += precio - descuento_producto
        total_sdescuento += precio

    elif opcion_descuento.lower() == "n":

        total_cdescuento += precio
        total_sdescuento += precio

promedio = total_cdescuento / cant_productos_a_comprar

print("-" * 40)
print(f"""Recibo de {nombre_cliente}
    Total sin descuentos: ${total_sdescuento}
    Total con descuento: ${total_cdescuento:.2f}
    Ahorro total: ${ahorro_total:.2f}
    Promedio por producto: ${promedio:.2f}
    """)

