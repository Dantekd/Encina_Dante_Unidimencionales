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


