import core
import os

diccCompra = {"data":[]}

def LoadInfoCompra():
    global diccCompra
    if (core.checkFile("compras.json")):
        diccCompra = core.LoadInfo("compras.json")
    else:
        core.crearInfo("compras.json",diccCompra)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^20}{}{:^23}|".format(' ','ADMINISTRACION DE COMPRAS',' '))
    print('+','-'*55,'+')
    print("1. Registrar compra")
    print("2. Buscar compra")
    print("3. Devoución de compra")
    print("4. Anular factura de compra")
    print("5. Regresar al menú principal")
    opcion =int(input("-->  "))
    if (opcion == 1):
        while True:
            idPurchase = input("Ingrese el Id del compra: ")
            idExistente = False
            
            for i in diccCompra["data"]:
                if (i["id"] == idPurchase):
                    idExistente = True
                    break

            if (idExistente):
                print("El Id ya existe, ingrese otro")
            else:
                data = {
                    "id":idPurchase,
                    "nombre":input("Ingrese el Nombre del titular de la compra: "),
                    "email":input("Ingrese el Email del titular: "),
                }
                core.crearInfo("compras.json",data)
                diccCompra["data"].append(data)
                break
                
    elif (opcion == 2):
        purchaseWanted = input("Ingrese el Id del compra: ")
        purchaseFound = False
        for i in diccCompra["data"]:
            if (i["id"] == purchaseWanted):
                print("Id: ",i["id"])
                print("Nombre: ",i["nombre"].upper())
                print("Email: ",i["email"])
                purchaseFound = True
                break

        if (not purchaseFound):
            print("No se encontró ninguna compra con el ID especificado.")
        input("Presione una tecla para continuar...")
    elif (opcion == 3):
        purchaseWanted = input("Ingrese el Id del compra: ")
        purchaseFound = False
        for i in diccCompra["data"]:
            if (i['id'] == purchaseWanted):
                i["nombre"] = input("Ingrese el nuevo Nombre del titular de la compra: ") or i["nombre"]
                i["email"] = input("Ingrese el nuevo Email de la compra: ") or i["email"]
                purchaseFound = True
                core.EditarData("compras.json",diccCompra)
                break

        if (not purchaseFound):
            print("No se encontró ninguna compra con el ID especificado.")
        input("Presione una tecla para continuar...")
    elif (opcion == 4):
        purchaseWanted = input("Ingrese el Id de la compra a eliminar: ")
        purchaseFound = False
        for i in diccCompra["data"]:
            if (i['id'] == purchaseWanted):
                diccCompra["data"].remove(i)
                purchaseFound = True
                core.EditarData("compras.json",diccCompra)
                break

        if (not purchaseFound):
            print("No se encontró ningún compra con el ID especificado.")
        input("Presione una tecla para continuar...")
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()