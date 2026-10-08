Flota_aerea = []

while True:
    print("n---Sistema de manteninmiento de aeronaves---")
    print("1.Registrar Aeronave")
    print("2.Registro de componentes")
    print("3.Consultar Mantenimiento previo")
    print("4.Salir del menu")

    opcion = input("Ingrese el numero de la informacion que desea:")
    if opcion == "1":
        matricula = input("Ingrese el numero de matricula")
        horas = float(input("ingrese el numero de horas"))
        modelo = input("Ingrese el modelo")
        nueva_aeronave = {
            "matricula":matricula,
            "modelo" : modelo,
            "horas" : horas,
            "componentes":[]
        }
        Flota_aerea.append(nueva_aeronave)
        print("Aeronave registrada con exito")
    elif opcion == "2":
        buscar_matricula = input("Ingrese la matricula de la aeronave:")
        avion_encontrado = False
        for avion in Flota_aerea:
            if avion["matricula"] == buscar_matricula:
                avion_encontrado = True
                print(f"avion {buscar_matricula} encontrado")
                pieza = input("ingrese nombre de la pieza")
                horas_Uso_Actuales = float(input("ingrese la cantidad de horas de uso actuales"))
                limite_Horas = float(input("Ingrese el limite de horas permitido"))
                nuevo_componente = {
                    "horas de uso actuales": horas_Uso_Actuales,
                    "pieza" : pieza,
                    "limite de horas permitidas": limite_Horas
                }
                avion["componentes"].append(nuevo_componente)
                print(f"\nComponente:{pieza} registrado con exito")
        if avion_encontrado == False:
            print("Error:Aeronave no encontrada")
    elif opcion == "3":
        print("n---Componente en condiciones de operacion---")
        for avion in Flota_aerea:
            for componente in avion["componentes"]:
                if componente["horas de uso actuales"] >= componente["limite de horas permitidas"]:
                 print(f"Alerta,El avion {avion["matricula"]} requiere cambio de {componente["pieza"]}")
                 respuesta = input("Desea registrar cambios en el componente").lower().strip()
                 if respuesta == "s":
                     componente["horas de uso actuales"] = 0.0
                     print(f"exito, Las horas de {componente["pieza"]} se han reiniciado a 0.0")
                else: 
                 print("Componente en condiciones de operacion")         
    elif opcion == "4": break
    else:
        print("opcion invalida, ingrese un valor computable") 




