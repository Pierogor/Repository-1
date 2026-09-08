def menu():
    print ("1. plato fuerte\n2.Bebidas\n3.Postres\n4.Salir")
opcion= int(input("ingresa la primera opcion"))

control = True
while control == True:
    opcion = menu()
print ("1. plato fuerte\n2.Bebidas\n3.Postres\n4.Salir")
opcion= int(input("ingresa la primera opcion"))
while opcion != 4:
    if opcion ==1:
        print("platos fuertes")
        print("1.hamburguesa\n2.lasagna\n3.arroz con agua")
        plato = input("Elija un plato")
        print("\n\n")
        print(f"usted eligio:{plato}")
        print("\n\n")
    elif opcion == 2:
        print("Bebidas")
    elif opcion == 3:
        print("Postres")
    elif opcion == 4:
        print ("Saliendo del menu")
        break 
    control = False
    print ("opcion invalida")
print ("1. plato fuerte\n2.Bebidas\n3.Postres\n4.Salir")
opcion= int(input("ingresa la primera opcion"))
    