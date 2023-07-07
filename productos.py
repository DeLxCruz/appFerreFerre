import core
import os
def CreateData(*args):
    return core.LoadInfo("productos.json")

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^20}{}{:^23}|".format(' ','ADMINISTRACION DE PRODUCTOS',' '))
    print('+','-'*55,'+')

    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Editar producto")
    print("4. Anular producto")
    print("5. Activar o desactivar producto")
    print("6. Regresar al menú principal")
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