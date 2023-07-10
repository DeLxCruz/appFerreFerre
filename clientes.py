import core
import os

diccCliente = {"data":[]}

def LoadInfoCliente():
    global diccCliente
    if (core.checkFile("clientes.json")):
        diccCliente = core.LoadInfo("clientes.json")
    else:
        core.crearInfo("clientes.json",diccCliente)

def MainMenu():
    os.system("cls")
    isCliRun = True
    os.system("pause")
    os.system("cls")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE CLIENTES',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar cliente")
    print("3. Editar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar menu principal")
    opcion =int(input("-->  "))
    if (opcion == 1):
        while True:
            idCliente = input("Ingrese el Id del cliente: ")
            idExistente = False
            
            for i in diccCliente["data"]:
                if (i["id"] == idCliente):
                    idExistente = True
                    break

            if (idExistente):
                print("El Id ya existe, ingrese otro")
            else:
                data = {
                    "id":idCliente,
                    "nombre":input("Ingrese el Nombre del cliente: "),
                    "email":input("Ingrese el Email del cliente: "),
                }
                core.crearInfo("clientes.json",data)
                diccCliente["data"].append(data)
                break
                
    elif (opcion == 2):
        clientWanted = input("Ingrese el Id del cliente: ")
        clientFound = False
        for i in diccCliente["data"]:
            if (i["id"] == clientWanted):
                print("Id: ",i["id"])
                print("Nombre: ",i["nombre"].upper())
                print("Email: ",i["email"])
                clientFound = True
                break

        if (not clientFound):
            print("No se encontró ningún cliente con el ID especificado.")
        input("Presione una tecla para continuar...")
    elif (opcion == 3):
        clientWanted = input("Ingrese el Id del cliente: ")
        clientFound = False
        for i in diccCliente["data"]:
            if (i['id'] == clientWanted):
                i["nombre"] = input("Ingrese el nuevo Nombre del cliente: ") or i["nombre"]
                i["email"] = input("Ingrese el nuevo Email del cliente: ") or i["email"]
                clientFound = True
                core.EditarData("clientes.json",diccCliente)
                break

        if (not clientFound):
            print("No se encontró ningún cliente con el ID especificado.")
        input("Presione una tecla para continuar...")
    elif (opcion == 4):
        clientWanted = input("Ingrese el Id del cliente a eliminar: ")
        clientFound = False
        for i in diccCliente["data"]:
            if (i['id'] == clientWanted):
                diccCliente["data"].remove(i)
                clientFound = True
                core.EditarData("clientes.json",diccCliente)
                break

        if (not clientFound):
            print("No se encontró ningún cliente con el ID especificado.")
        input("Presione una tecla para continuar...")
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()

    