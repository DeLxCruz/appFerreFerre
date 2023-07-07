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
    os.system("clear")
    isCliRun = True
    os.system("pause")
    os.system("clear")
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
        data ={
            "id":input("Ingrese el Id del cliente :"),
            "nombre":input("Ingrese el Nombre del cliente :"),
            "email":input("Ingrese el Email del cliente :"),
        }
        core.crearInfo("clientes.json",data)
        diccCliente["data"].append(data)
    elif (opcion == 2):
        clientWanted = input("Ingrese el Id del cliente :")
        for i in diccCliente["data"]:
            if (i["id"] == clientWanted):
                print("Id: ",i["id"])
                print("Nombre: ",i["nombre"])
                print("Email: ",i["email"])
                input("Presione una tecla para continuar...")
                break

    elif (opcion == 3):
        clientWanted = input("Ingrese el Id del cliente :")
        for i in diccCliente["data"]:
            pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()

    