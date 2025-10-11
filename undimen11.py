def diferencia_arrays(array1: list[int], array2: list[int]):
    diferencia = []

    for i in range(len(array1)):
        esta_en_array2 = False
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                esta_en_array2 = True   
        repetido = False
        for k in range(len(diferencia)):
            if array1[i] == diferencia[k]:
                repetido = True
        if not esta_en_array2 and not repetido:
            diferencia.append(array1[i])

    print(f"La diferencia del primer array respecto al segundo es: {diferencia}")
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
diferencia_arrays(a, b)