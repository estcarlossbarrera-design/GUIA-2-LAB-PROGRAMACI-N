from ClaseMatriz import matriz
from orden import Orden
mat=matriz(0,0,0,0,0,0,0,0,0)

while True:
    print("Seleccione la opción que desea realizar:")
    print("1. Ordenamiento de números flotantes")
    print("2. Operaciones con matrices")
    print("3. Salir del programa")
    opcmenu=int(input("Ingrese el número de la opción deseada: "))
    match opcmenu:
        case 1:
            n = int(input("\n\tIngrese la cantidad de números flotantes: "))
            ords = Orden(n)
            print("\nLista original:")
            print(ords.original())
            
            print("\nOrdenamiento Burbuja:")
            print(ords.get_burbuja())
            
            print("\nOrdenamiento Inserción:")
            print(ords.get_insercion())
            
            print("\nOrdenamiento Selección:")
            print(ords.get_seleccion())
            
            print("\nOrdenamiento Mergesort:")
            print(ords.get_mergesort())
            
            print("\nOrdenamiento con sort() de Python:")
            print(ords.get_sort_python())
        case 2:
            print("Digite las matrices")
            mat.pedir()
            while True:
                print("Seleccione la operación que desea realizar:")
                print("1. Dar nuevas Matrices")
                print("2. Suma de matrices")
                print("3. Multiplicación de matrices")
                print("4. Multiplicación de matriz por vector")
                print("5. Hallar la inversa de la matriz")
                print("6. Salir al menu inicial")
                opc=int(input("Ingrese el número de la opción deseada: "))
                
                
                match opc:
                    case 1:
                        mat.pedir()
                    case 2:
                        mat.suma()
                        if mat.filas1 == mat.filas2 and mat.columnas1 == mat.columnas2:
                            mat.getresultado()
                    case 3:
                        mat.multiplicacion()
                        if mat.columnas1 == mat.filas2:
                            mat.getresultado()
                    case 4:
                        mat.multvector()
                        if mat.tamvector == mat.columnas2 or mat.tamvector == mat.columnas1:
                            mat.getresultado()
                    case 5:
                        mat.inversa()
                    case 6:
                        print("Saliendo al menu principal...")
                        break
                    case _:
                        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
        case 3:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")