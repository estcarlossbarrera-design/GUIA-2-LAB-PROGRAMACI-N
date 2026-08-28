class matriz:
    def __init__(self,matriz1,matriz2,vector,resultado,filas1,columnas1,filas2,columnas2,tamvector):
        self.matriz1 = matriz1
        self.matriz2 = matriz2
        self.vector = vector
        self.resultado = resultado
        self.filas1 = filas1
        self.columnas1 = columnas1
        self.filas2 = filas2
        self.columnas2 = columnas2
        self.matriz1=matriz1
        self.matriz2=matriz2
        self.vector=vector
        self.resultado=resultado
        self.tamvector=tamvector

    def pedir(self):
        print("Ingrese los datos de la matriz 1 y la matriz 2")
        self.filas1 = int(input("De cuantas filas sera la matriz 1? "))
        self.columnas1 = int(input("De cuantas columnas sera la matriz 1? "))
        self.filas2 = int(input("De cuantas filas sera la matriz 2? "))
        self.columnas2 = int(input("De cuantas columnas sera la matriz 2? "))

        self.matriz1 = [[0 for j in range(self.columnas1)] 
                        for i in range(self.filas1)]
        self.matriz2 = [[0 for j in range(self.columnas2)] 
                        for i in range(self.filas2)]
        self.resultado = [[0 for j in range(max(self.columnas1,self.columnas2))]
                        for i in range(max(self.filas1,self.filas2))]
        
        for i in range(self.filas1):
            for j in range(self.columnas1):
                self.matriz1[i][j] = int(input(f"Elemento [{i}][{j}] de la matriz 1: "))
        for i in range(self.filas2):
            for j in range(self.columnas2):
                self.matriz2[i][j] = int(input(f"Elemento [{i}][{j}] de la matriz 2: "))

    def suma(self):
        if self.filas1 == self.filas2 and self.columnas1 == self.columnas2:
                for i in range(self.filas1):
                    for j in range(self.columnas1):
                        self.resultado[i][j] = self.matriz1[i][j] + self.matriz2[i][j] 
        else:
            print("Las matrices no se pueden sumar, deben tener las mismas dimensiones.")

    def multiplicacion(self):
            if self.columnas1 == self.filas2:
                for i in range(self.filas1):
                    for j in range(self.columnas2):
                        self.resultado[i][j] = 0
                        for k in range(self.columnas1):
                            self.resultado[i][j] += self.matriz1[i][k] * self.matriz2[k][j]
            else:
                print("Las matrices no se pueden multiplicar, el número de columnas de la primera debe ser igual al número de filas de la segunda.")
                return
    
    def multvector(self):
        self.tamvector = int(input("Ingrese el tamaño del vector: "))

        self.vector = [0 for _ in range(self.tamvector)]

        for i in range(self.tamvector):
            self.vector[i] = int(input(f"Elemento [{i}] del vector: "))

        print("¿Desea multiplicar la matriz 1 o la matriz 2 por el vector?")
        opc = int(input("Ingrese la opción deseada: "))

        match opc:
            case 1:
                if self.tamvector == self.columnas1:
                    self.resultado = [0 for _ in range(self.filas1)]

                    for i in range(self.filas1):
                        for j in range(self.columnas1):
                            self.resultado[i] += self.matriz1[i][j] * self.vector[j]

                    print("Resultado de la multiplicación:")
                    print(self.resultado)

                else:
                    print("No se puede realizar la multiplicación.")
                    print("El tamaño del vector debe ser igual")
                    print("al número de columnas de la matriz 1.")

            case 2:
                if self.tamvector == self.columnas2:
                    self.resultado = [0 for _ in range(self.filas2)]

                    for i in range(self.filas2):
                        for j in range(self.columnas2):
                            self.resultado[i] += self.matriz2[i][j] * self.vector[j]

                    print("Resultado de la multiplicación:")
                    print(self.resultado)

                else:
                    print("No se puede realizar la multiplicación.")
                    print("El tamaño del vector debe ser igual")
                    print("al número de columnas de la matriz 2.")

            case _:
                print("Opción inválida. Por favor, elija 1 o 2.")

    def inversa(self):
        def determinante(matriz):
            n=len(matriz)
            if n==1:
                return matriz[0][0]
            det=0
            for j in range(n):
                submatriz = [
                    [matriz[i][k] for k in range(n) if k!=j]
                    for i in range(1,n)
                    ]
                det +=((-1)**j)*matriz[0][j]*determinante(submatriz)
            return det
        def calcular_inversa(matriz):
            n = len(matriz)
            det = determinante(matriz)
            if abs(det)<1e-11:
                return None
            cofactores = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    submatriz = [
                        [matriz[f][c] for c in range(n) if c != j]
                        for f in range(n) if f != i
                    ]
                    cofactores[i][j] = ((-1) ** (i+j)) * determinante(submatriz)
            inversa = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    inversa[i][j]=cofactores[j][i]/det
            return inversa
        print("Desea hallar la inversa de la matriz 1 o de la matriz 2?")
        opc = int(input("Ingrese la opción deseada: "))
        match opc:
            case 1:
                if self.filas1==self.columnas1:
                    inversa=calcular_inversa(self.matriz1)
                    if inversa is None:
                        print("La matriz no tiene inversa porque su determinante es cero.")
                    else:
                        self.resultado=inversa
                        print("\nLa matriz inversa resultante es:")
                        for fila in inversa:
                            print([round(valor,4) for valor in fila])
                else:
                    print("La matriz 1 no es cuadrada, no se puede calcular su inversa.")
            case 2:
                if self.filas2==self.columnas2:
                    inversa=calcular_inversa(self.matriz2)
                    if inversa is None:
                        print("La matriz no tiene inversa porque su determinante es cero.")
                    else:
                        self.resultado=inversa
                        print("\nLa matriz inversa resultante es:")
                        for fila in inversa:
                            print([round(valor,4) for valor in fila])
                else:
                    print("La matriz 2 no es cuadrada, no se puede calcular su inversa.")
            case _:
                print("Opción inválida. Por favor, elija 1 o 2.")

    def getresultado(self):
        for i in range(len(self.resultado)):
            print(self.resultado[i])
