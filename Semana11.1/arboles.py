# IMPLEMENTACIÓN GUIADA EN PYTHON

# Paso A: Crear nodos e insertar

def crear_nodo(valor):
    return {"dato": valor, "izq": None, "der": None}

def insertar_raiz(raiz, valor):
    if raiz is None:
        return crear_nodo(valor)
    if valor < raiz ["valor"]:
        raiz["izq"]