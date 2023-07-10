import core
import os

diccVenta = {"data":[]}

def LoadInfoVenta():
    global diccVenta
    if (core.checkFile("ventas.json")):
        diccVenta = core.LoadInfo("ventas.json")
    else:
        core.crearInfo("ventas.json",diccVenta)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^20}{}{:^23}|".format(' ','ADMINISTRACION DE VENTAS',' '))
    print('+','-'*55,'+')
    print("1. Registrar venta")
    print("2. Buscar venta")
    print("3. Devoución de venta")
    print("4. Anular factura de venta")
    print("5. Regresar al menú principal")
    opcion =int(input("-->  "))
    if (opcion == 1):
        while True:
            idventa = input("Ingrese el Id de la venta: ")
            idExistente = False
            
            for i in diccVenta["data"]:
                if (i["id"] == idventa):
                    idExistente = True
                    break

            if (idExistente):
                print("El Id ya existe, ingrese otro")
            else:
                data = {
                    "id":idventa,
                    "nombre":input("Ingrese el Nombre del titular de la venta: "),
                    "email":input("Ingrese el Email del titular de la venta: "),
                }
                core.crearInfo("ventas.json",data)
                diccVenta["data"].append(data)
                break
                
    elif (opcion == 2):
        saleWanted = input("Ingrese el Id del venta: ")
        saleFound = False
        for i in diccVenta["data"]:
            if (i["id"] == saleWanted):
                print("Id: ",i["id"])
                print("Nombre: ",i["nombre"].upper())
                print("Email: ",i["email"])
                saleFound = True
                break

        if (not saleFound):
            print("No se encontró ningún venta con el ID especificado.")
        input("Presione una tecla para continuar...")
    elif (opcion == 3):
        saleWanted = input("Ingrese el Id del venta: ")
        saleFound = False
        for i in diccVenta["data"]:
            if (i['id'] == saleWanted):
                i["nombre"] = input("Ingrese el nuevo Nombre del venta: ") or i["nombre"]
                i["email"] = input("Ingrese el nuevo Email del venta: ") or i["email"]
                saleFound = True
                core.EditarData("ventas.json",diccVenta)
                break

        if (not saleFound):
            print("No se encontró ningún venta con el ID especificado.")
        input("Presione una tecla para continuar...")
    elif (opcion == 4):
        saleWanted = input("Ingrese el Id del venta a eliminar: ")
        saleFound = False
        for i in diccVenta["data"]:
            if (i['id'] == saleWanted):
                diccVenta["data"].remove(i)
                saleFound = True
                core.EditarData("ventas.json",diccVenta)
                break

        if (not saleFound):
            print("No se encontró ninguna venta con el ID especificado.")
        input("Presione una tecla para continuar...")
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()