import core
import os
def CreateData(*args):
    return core.LoadInfo("ventas.json")

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