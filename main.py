bandas = []
banda = {}

opcion = 100
while(opcion != 5):
   

    print("***FESTIVAL ALTAVOZ***")
    print("**********************")
    print("1. Registar Banda")
    print("2. Ver cartel del festival")
    print("3. Buscar banda")
    print("4. Modificar Banda")
    print("5. Finalizar")

    opcion = int(input("Digita una opcion: "))
    
    if opcion == 1:
        banda = {}
        banda["id"] = int(input("Digite el id: "))        
        banda["nombre"] = input("Digite el nombre: ")        
        banda["genero"] = input("Digite el Genero: ")
        banda["coste"] = int(input("Digite el costo del toque:  "))
        # agregar diccionario a la lista
        bandas.append(banda)   
    elif opcion == 2:
        # recorriendo la lista bandas para recorrer sus elementos
        for bandaAuxiliar in bandas:
            print(f"Id de la banda: {bandaAuxiliar["id"]} -- Nombre de la banda:  {bandaAuxiliar["nombre"]}")

    elif opcion == 3:
         # Buscador de elementos dentro de la lista
        bandaBuscada = input("Digite la banda que quieres buscar: ")
        for bandaAuciliar in bandas:
            if bandaAuciliar["nombre"] == bandaBuscada:
                print("Banda encontrada")
            else:
                print("banda no encontrada")

    elif opcion == 4:
         bandaEditada = input
    elif opcion == 5:
        print("Finalizar")
    else:
         print("Opcion invalidad")