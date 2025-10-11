def calcular_maximo (lista_numeros: list) -> int:
    bandera=True
    maximo=0
    for i in range(len(lista_numeros)):
        if bandera == True or lista_numeros[i]> maximo:
            bandera= False
            maximo= lista_numeros[i]
    return maximo
lista_numeros = [12,14,6,8]
print(f"El numero maximo es {calcular_maximo(lista_numeros)}")
def mostrar_posicion_maximo(lista_numeros: list[int]):
    maximo= calcular_maximo(lista_numeros)
    posicion=[]
    for i in range (len(lista_numeros)):
        if lista_numeros[i]==maximo:
            posicion.append(i)
    return posicion
lista_numeros = [12,14,6,8]
posicion = mostrar_posicion_maximo(lista_numeros)
maximo = calcular_maximo(lista_numeros)
print(f"El valor máximo {maximo} se encuentra en las posiciones: {posicion}")

mostrar_posicion_maximo(lista_numeros)