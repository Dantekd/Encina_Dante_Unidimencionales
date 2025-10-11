def promedio_lista(numeros: list[int]) -> float:
    suma=0
    contador=0
    for n in numeros:
        if n > 0:
            contador+=1
            suma+=n
    if len(numeros)==0:
        promedio=0
    else:
        promedio=suma/contador
    return promedio
lista = [10, -39, 30, 40, 50]
print(f"El promedio es: {promedio_lista(lista)}")