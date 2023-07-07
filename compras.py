import core
import os
def CreateData(*args):
    return core.LoadInfo("compras.json")

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