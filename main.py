from ClaseMatriz import matriz
mat=matriz(0,0,0,0,0,0,0,0,0)
print("Digite las matrices")
mat.pedir()


while True:
    print("Seleccione la operación que desea realizar:")
    print("1. Dar nuevas Matrices")
    print("2. Suma de matrices")
    print("3. Multiplicación de matrices")
    print("4. Multiplicación de matriz por vector")
    print("5. Hallar la inversa de la matriz")
    print("6. Salir")
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
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")