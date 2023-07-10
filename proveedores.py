import core
import os

diccProveedor = {"data":[]}

def LoadInfoProveedor():
    global diccProveedor
    if (core.checkFile("proveedores.json")):
        diccProveedor = core.LoadInfo("proveedores.json")
    else:
        core.crearInfo("proveedores.json",diccProveedor)

def MainMenu():
    os.system("cls")
    isCliRun = True
    os.system("cls")
    print("╔═════════════════════════════════════════╗")
    print("║     ¡Administración de Proovedores!     ║")
    print("╠═════════════════════════════════════════╣")
    print("║      Seleccione una opción:             ║")
    print("║                                         ║")
    print("║    1. Registrar Proveedor               ║")
    print("║    2. Buscar Proveedor                  ║")
    print("║    3. Editar Proveedor                  ║")
    print("║    4. Eliminar Proveedor                ║")
    print("║    5. Regresar al menú principal        ║")
    print("║                                         ║")
    print("╚═════════════════════════════════════════╝")
    opcion =int(input("-->  "))
    if (opcion == 1):
        while True:
            idProveedor = input("Ingrese el Id del proveedor: ")
            idExistente = False
            
            for i in diccProveedor["data"]:
                if (i["id"] == idProveedor):
                    idExistente = True
                    break

            if (idExistente):
                print("El Id ya existe, ingrese otro")
            else:
                data = {
                    "id":idProveedor,
                    "nombre":input("Ingrese el Nombre del cliente: "),
                    "email":input("Ingrese el Email del cliente: "),
                }
                core.crearInfo("proveedores.json",data)
                diccProveedor["data"].append(data)
                break
                
    elif (opcion == 2):
        supplierWanted = input("Ingrese el Id del proveedor: ")
        supplierFound = False
        for i in diccProveedor["data"]:
            if (i["id"] == supplierWanted):
                print("Id: ",i["id"])
                print("Nombre: ",i["nombre"].upper())
                print("Email: ",i["email"])
                supplierFound = True
                break

        if (not supplierFound):
            print("No se encontró el proveedor")
        input("Presione una tecla para continuar...")
    elif (opcion == 3):
        supplierWanted = input("Ingrese el Id del proveedor: ")
        supplierFound = False
        for i in diccProveedor["data"]:
            if (i['id'] == supplierWanted):
                i["nombre"] = input("Ingrese el nuevo Nombre del cliente: ") or i["nombre"]
                i["email"] = input("Ingrese el nuevo Email del cliente: ") or i["email"]
                supplierFound = True
                core.EditarData("proveedores.json",diccProveedor)
                break
        
        if (not supplierFound): 
            print("No se encontró el proveedor")
        input("Presione una tecla para continuar...")
    elif (opcion == 4):
        supplierWanted = input("Ingrese el Id del proveedor a eliminar: ")
        supplierFound = False
        for i in diccProveedor["data"]:
            if (i['id'] == supplierWanted):
                diccProveedor["data"].remove(i)
                supplierFound = True
                core.EditarData("proveedores.json",diccProveedor)
                break

        if (not supplierFound):
            print("No se encontró el proveedor")
        input("Presione una tecla para continuar...")
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()
    
