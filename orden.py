import random

class Orden:
    def __init__(self, n):
        self.lista = [random.random() for _ in range(n)]

    def get_lista_original(self):
        return self.lista.copy()

    def get_burbuja(self):
        return self.burbuja(self.lista.copy())

    def get_insercion(self):
        return self.insercion(self.lista.copy())

    def get_seleccion(self):
        return self.seleccion(self.lista.copy())

    def get_mergesort(self):
        return self.mergesort(self.lista.copy())

    def get_sort_python(self):
        return sorted(self.lista)


    def burbuja(self, lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def insercion(self, lista):
        for i in range(1, len(lista)):
            key = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > key:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
        return lista

    def seleccion(self, lista):
        n = len(lista)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if lista[j] < lista[min_idx]:
                    min_idx = j
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
        return lista

    def mergesort(self, lista):
        if len(lista) <= 1:
            return lista

        mid = len(lista) // 2
        left = self.mergesort(lista[:mid])
        right = self.mergesort(lista[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        resultado = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                resultado.append(left[i])
                i += 1
            else:
                resultado.append(right[j])
                j += 1

        resultado.extend(left[i:])
        resultado.extend(right[j:])
        return resultado
