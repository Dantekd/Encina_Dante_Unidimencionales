def mostrar_lista(lista_nombres: list):
    print("Lista de nombres: ")
    for i in range(len(lista_nombres)):
        print(lista_nombres[i])

def reemplazar(lista, valor_busqueda, valor_reemplazo):
    for i in range (len(lista)):
        if valor_busqueda ==lista[i]:
            lista[i]= valor_reemplazo
lista_nombres= ["Manuel", "Maria", "Maria", "Pepe", "Dominica"]
reemplazar(lista_nombres,"Maria","Roberto")
mostrar_lista(lista_nombres)