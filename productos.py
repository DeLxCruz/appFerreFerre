import core
import os

diccProducto = {"data":[]}

def LoadInfoProducto():
    global diccProducto
    if (core.checkFile("productos.json")):
        diccProducto = core.LoadInfo("productos.json")
    else:
        core.crearInfo("productos.json",diccProducto)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print("╔═══════════════════════════════════════╗")
    print("║     ¡Administración de Productos!     ║")
    print("╠═══════════════════════════════════════╣")
    print("║      Seleccione una opción:           ║")
    print("║                                       ║")
    print("║    1. Registrar Producto              ║")
    print("║    2. Buscar Producto                 ║")
    print("║    3. Editar Producto                 ║")
    print("║    4. Anular Producto                 ║")
    print("║    5. Activar o desactivar Producto   ║")
    print("║    6. Regresar al menú principal      ║")
    print("║                                       ║")
    print("╚═══════════════════════════════════════╝")
    opcion =int(input("-->  "))
    if (opcion == 1):
        while True:
            idProveedor = input("Ingrese el Id del producto: ")
            idExistente = False
            
            for i in diccProducto["data"]:
                if (i["id"] == idProveedor):
                    idExistente = True
                    break

            if (idExistente):
                print("El Id ya existe, ingrese otro")
            else:
                data = {
                    "id":idProveedor,
                    "nombre":input("Ingrese el Nombre del cliente: "),
                    "cantidad": 0,
                    'stockMin': int(input("Ingrese el stock minimo: ")),
                    'stockMax': int(input("Ingrese el stock maximo: ")),
                    'valorCompra': float(input("Ingrese el valor de compra: ")),
                    'precio': float(input("Ingrese el valor de venta: ")),
                    'estado': True
                }
                core.crearInfo("productos.json",data)
                diccProducto["data"].append(data)
                break
                
    elif (opcion == 2):
        productWanted = input("Ingrese el Id del producto: ")
        productFound = False
        for i in diccProducto["data"]:
            if (i["id"] == productWanted):
                print("Id: ",i["id"])
                print("Nombre: ",i["nombre"].upper())
                print("Cantidad: ",i["cantidad"])
                print('Precio: ',i['precio'])
                productFound = True
                break

        if (not productFound):
            print("No se encontró el producto")
        input("Presione una tecla para continuar...")
    elif (opcion == 3):
        productWanted = input("Ingrese el Id del prodcuto: ")
        productFound = False
        for i in diccProducto["data"]:
            if (i['id'] == productWanted):
                i["nombre"] = input("Ingrese el nuevo Nombre del producto: ") or i["nombre"]
                i["precio"] = input("Ingrese el nuevo valor de venta del producto: ") or i["precio"]
                productFound = True
                core.EditarData("productos.json",diccProducto)
                break

        if (not productFound):
            print("No se encontró el producto")
        input("Presione una tecla para continuar...")
    elif (opcion == 4):
        productWanted = input("Ingrese el Id del cliente: ")
        productFound = False
        for i in diccProducto["data"]:
            if (i['id'] == productWanted):
                diccProducto["data"].remove(i)
                productFound = True
                core.EditarData("productos.json",diccProducto)
                break
        if (not productFound):
            print("No se encontró el producto")
        input("Presione una tecla para continuar...")
    elif (opcion == 5):
        pass
    elif (opcion == 6):
        isCliRun = False
    if (isCliRun):
        MainMenu()