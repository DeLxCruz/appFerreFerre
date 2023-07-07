import core
import os
def CreateData(*args):
    return core.LoadInfo("proveedores.json")

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^20}{}{:^23}|".format(' ','ADMINISTRACION DE PROVEEDORES',' '))
    print('+','-'*55,'+')

    print("1. Registrar proveedor")
    print("2. Buscar proveedor")
    print("3. Editar proveedor")
    print("4. Eliminar proveedor")
    print("5. Regresar al menú principal")
    opcion =int(input("-->"))
    if (opcion == 1):
        pass
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        isCliRun = False
    if (isCliRun):
        MainMenu()

    
