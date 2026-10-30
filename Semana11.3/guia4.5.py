# 4.5. Operaciones introductorias sobre árboles binarios
print(("\n4.5. Operaciones introductorias sobre árboles binarios").title())

from collections import deque

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


def insertar(raiz, dato):
    nuevo = Nodo(dato)
    if raiz is None:
        return nuevo
    cola = deque([raiz])

    while cola:
        actual = cola.popleft()
        if actual.izquierdo is None:
            actual.izquierdo = nuevo
            return raiz
        else:
            cola.append(actual.izquierdo)
        if actual.derecho is None:
            actual.derecho = nuevo
            return raiz
        else:
            cola.append(actual.derecho)


def buscar(nodo, dato):
    if nodo is None:
        return False
    if nodo.dato == dato:
        return True
    return buscar(nodo.izquierdo, dato) or buscar(nodo.derecho, dato)


def eliminar_hoja(nodo, dato):
    if nodo is None:
        return None
    if nodo.dato == dato and nodo.izquierdo is None and nodo.derecho is None:
        return None
    nodo.izquierdo = eliminar_hoja(nodo.izquierdo, dato)
    nodo.derecho = eliminar_hoja(nodo.derecho, dato)
    return dato


def mostrar(nodo, nivel = 0):
    if nodo is not None:
        mostrar(nodo.derecho, nivel + 1)
        print("   " * nivel + str(nodo.dato))
        mostrar(nodo.izquierdo, nivel + 1)


raiz  = None

while True:
    print(("\n--- Menú de árboles binarios ---").title())
    print("1. Insertar nodo.")
    print("2. Mostrar árbol.")
    print("3. Buscar dato.")
    print("4. Eliminar hoja.")
    print("5. Salir.")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        dato = input("Ingrese el dato: ")
        raiz = insertar(raiz, dato)
        print("Nodo insertado.")

    elif opcion == "2":
        if raiz is None:
            print("Árbol vacío.")
        else:
            mostrar(raiz)

    elif opcion == "3":
        dato = input("Dato a buscar: ")
        if buscar(raiz, dato):
            print("Dato encontrado.")
        else:
            print("Dato no encontrado.")


    elif opcion == "4":
        dato = input("Dato de la hoja a eliminar: ")
        if buscar(raiz, dato):
            if raiz.dato == dato and raiz.izquierdo is None and raiz.derecho is None:
                raiz = None
                print("Hoja eliminada.")
            else:
                raiz = eliminar_hoja(raiz, dato)
                print("Eliminación realizada si el dato era una hoja.")
        else:
            print("Dato no encontrado.")


    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
        




# Si se elimina un dato, muestra error en la línea 53, en mostrar(nodo.derecho, nivel + 1); en la parte de nodo.derecho