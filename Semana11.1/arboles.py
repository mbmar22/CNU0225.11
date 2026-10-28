# IMPLEMENTACIÓN GUIADA EN PYTHON

# Paso A. Crear nodos e insertar
print(("Paso A. Crear nodos e insertar").title())

def crear_nodo(valor):
    return {"dato": valor, "izq": None, "der": None}

def insertar(raiz, valor):
    if raiz is None:
        return crear_nodo(valor)
    if valor < raiz["valor"]:
        raiz["izq"] = insertar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = insertar(raiz["der"], valor)
    return raiz

raiz = None
for numero in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, numero)



# Paso B. Buscar e imprimir inorden.
print(("Paso B. Buscar e imprimir inorden").title())

def buscar(raiz, valor):
    if raiz is None:
        return False
    if raiz["valor"] == valor:
        return valor
    if valor < raiz["valor"]:
        return buscar(raiz["izq"], valor)
    return buscar(raiz["der"], valor)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz["izq"])
        print(raiz["valor"], end = "")
        inorden(raiz["der"])

print(buscar(raiz, 60))
inorden(raiz)