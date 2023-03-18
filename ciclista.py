from os import remove

opcion = 1 
ciclistas = []


while opcion != 0:
    print("Opciones")
    print()
    print("Opcion 1 = Ingresar 1 ciclista")
    print("Opcion 2 = Mostrar los ciclistas")
    print("Opcion 3 = Buscar 1 ciclista")
    print("Opcion 4 = Editar 1 ciclista")
    print("Opcion 5 = Eliminar 1 ciclista")
    print("Opcion O = Salir ")
    print()
    
    opcion = int(input("Seleccione una opcion:"))
    
    if(opcion == 1):
        ciclista = {}
        print("Ingresar Ciclista")
        ciclista['cedula']  = len(ciclistas)+1
        ciclista['nombre']  = input("Digite el nombre del ciclista: ")
        ciclista['edad']    = int(input("Digite la edad del ciclista: "))
        ciclista['pais']    = input("Digite el pais del ciclista: ")
        ciclista['equipo']  = input("Digite el equipo del ciclista: ")
        ciclista['tiempo']  = int(input("Digite el tiempo del ciclista: "))
        ciclistas.append(ciclista)
        print()
        print("ciclista registrado con exito")
        print()
        
    elif(opcion == 2):
        if(len(ciclistas) > 0):
            print("Ciclistas registrados")
            print(f"{ciclistas}")
        else:
            print("la lista no tiene elementos")
            
    elif(opcion == 3):
        print()
        print("Buscar ciclista")
        buscando = int(input("Ingrese el codigo del ciclista a buscar:"))
        for ciclista in ciclistas:
            if(buscando == ciclista['cedula']):
                print(f"ciclista encontrado {ciclista}")
                print()
            else:
                print("ciclista no encontrado")
    elif(opcion == 4):
        print("Editar ciclista")
        print()
        buscando = int(input("Ingrese el codigo del ciclista a editar: "))
        for ciclista in ciclistas:
            if(buscando == ciclista['cedula']):
                print (f"ciclista a editar {buscando}")
                ciclista['timepo'] = int(input("Ingrese el nuevo tiempo del ciclista :"))
                print("tiempo actualizado")
            else:
                print("ciclista no encontrado")
    elif(opcion == 5):
        print("Eliminar ciclista")
        print()
        buscando = int(input("Digite el codigo del ciclista a eliminar:"))
        for ciclista in ciclistas:
            if(buscando == ciclista['cedula']):

                print(f"Ciclista eliminar {ciclista}")
                ciclistas.remove(ciclista)
                print("Se elimino el ciclista")
                break
            else:
                print("ciclista no encontrado")
    else:
        print("Opcion digitada no existe, vuelva a intentar")