import clientes
import compras
import ventas
import productos
import proveedores
import os
if __name__ == "__main__":
    isActivate = True
    opcion = 0
    dataproductos={'data':[]}
    dataproveedores={'data':[]}
    datacompras={'data':[]}
    dataventas={'data':[]}
    while (isActivate):
        print('+','-'*55,'+')
        print("|{:^20}{}{:^23}|".format(' ','MENU PRINCIPAL',' '))
        print('+','-'*55,'+')
        print("1. Gestión de Clientes")
        print("2. Gestión de Productos")
        print("3. Gestión de Proveedores")
        print("4. Gestión de Compras")
        print("5. Gestión de Ventas")
        print("6. Salir")
        opcion =int(input("-->"))
        if (opcion == 1):
            clientes.LoadInfoCliente()
            clientes.MainMenu()
        elif (opcion == 2):
            productos.LoadInfoProducto()
            productos.MainMenu()
        elif (opcion == 3):
            proveedores.LoadInfoProveedor()
            proveedores.MainMenu()
        elif (opcion == 4):
            compras.LoadInfoCompra()
            compras.MainMenu()
        elif (opcion == 5):
            ventas.LoadInfoVenta()
            ventas.MainMenu()
        elif (opcion == 6):
            isActivate = False