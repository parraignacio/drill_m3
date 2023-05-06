lista = ["Harry Houdini", "David Blaine", "Teller", "Newton", "Hawking", "Einstein", "Messi", "Pele", "Juanes"]

magos = lista[:3]

cientificos = lista[3:6]

otros = []
for i in lista:
    if i not in magos + cientificos:
        otros.append(i)


def hacer_grandioso(a):
    b = a[:]
    for i in range(len(b)):
        b[i] = "El gran " + b[i]
    return b

magos_mod = hacer_grandioso(magos)

def imprimir_nombres(a):
    if isinstance(a, list):
        for i in a:
            print(i)
    else:
        print("Ingrese una lista como argumento.")
 
        
def imprimir_clase(lista, clase=None):
    opciones = {
        "m": {"titulo": "Magos", "personajes": lista[:3]},
        "c": {"titulo": "Cientificos", "personajes": lista[3:6]},
        "o": {"titulo": "Otros", "personajes": otros}
    }
    
    clase = clase.lower() if clase else None
    eleccion = opciones.get(clase)
    
    if eleccion:
        titulo = eleccion['titulo']
        personajes = eleccion['personajes']
        print(f"{titulo}:")
        for i in personajes:
            print(f"- {i}")
    elif clase:
        print("Ingrese una clase válida u omita el segundo argumento para imprimir la lista completa.")
    else:
        print("Lista completa:")
        for i in lista:
            print(f"- {i}")
 
 
clases = [None, "m", "c", "o"]   

for arg in clases:
    imprimir_clase(lista, arg)
    print()

imprimir_nombres(magos_mod)
