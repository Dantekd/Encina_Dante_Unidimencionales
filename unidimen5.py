def multi_lista(numeros: list[int]) -> float:
    multi=1
    for n in numeros:
            multi*=n
    if len(numeros)==0:
        multi=0
    return multi
lista = [10, 20, 30, 40, 50]
print(f"La multiplicion de todos los numeros es: {multi_lista(lista)}")