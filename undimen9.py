def interseccion_arrays(array1: list[int], array2: list[int]):
    interseccion = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                repetido = False
                for k in range(len(interseccion)):
                    if array1[i] == interseccion[k]:
                        repetido = True
                if not repetido:
                    interseccion.append(array1[i])
    print(f"La intersección de los dos arrays es: {interseccion}")

# Ejemplo de uso
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
interseccion_arrays(a, b)