 #productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],...]

productos = { 
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],...
} 
#stock = {modelo: [precio, stock]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
 }
def Pybooks(marca):
    total_stock=0
    for  modelo,info,in notebook.items():
        if info[0].lower()==marca.lower():
            total_stock+=stock.get(modelo, [0,0])[1]
            print(f"stock total de (marca.title)()":(total_stock):)
            def bucar_precios(p_main,p_max):
                encontrados=False
                for modelo,datos[1]
                if p_main <= precio <= p_max:
                    print (f"{modelo}:${precio}")
                    encontrados = True
                    if not encontrados:
                        print ("no se encontraron notebooks con estas caracteristicas")
                        def actualizarPrecios(modelo,nuevo_precio):
                            form modelo in total_stock():
                            if stock[modelo]==modelo:
                                stock[modelo]=nuevo_precio
                                return True
                            else:
                                return False
                        while True:
                            print(""*** MENU PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Actualizar precio.
4. Salir.
"")
                            try: opcion=int(input("ingrese una opcion:"))
                            if opcion<1 or opcion>4:
                                print ("ingrese una opcion correcta.")
                            except ValueError:


























