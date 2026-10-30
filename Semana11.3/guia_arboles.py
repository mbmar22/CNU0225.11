# 4.1 ¿Qué es un árbol?
print(("\n4.1. ¿Qué es un árbol?").title())
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

raiz = Nodo("Ana")
raiz.izquierdo = Nodo("Luis")
raiz.derecho = Nodo("María")

print("Raíz:", raiz.dato)
print("Hijo izquierdo:", raiz.izquierdo.dato)
print("Hijo derecho:", raiz.derecho.dato)


# 4.3. Crear y enlazar nodos
print(("\n4.3. Crear y enlazar nodos").title())
raiz = Nodo("A")
raiz.izquierdo = Nodo("B")
raiz.derecho = Nodo("C")

print("Raíz:", raiz.dato)
print("Hijo izquierdo:", raiz.izquierdo.dato)
print("Hijo derecho:", raiz.derecho.dato)


# 4.4. Representación y recorrido
print(("\n4.4. Representación y recorrido").title())

def recorrer(nodo):
    if nodo is not None:
        print(nodo.dato)
        recorrer(nodo.izquierdo)
        recorrer(nodo.derecho)

print("Recorrido del árbol:")
recorrer(raiz)