def union_arrays(array1: list[int], array2: list[int]):
    union = []
    for i in range(len(array1)):
        repetido = False
        for k in range(len(union)):
            if array1[i] == union[k]:
                repetido = True
        if not repetido:
            union.append(array1[i])

    for j in range(len(array2)):
        repetido = False
        for k in range(len(union)):
            if array2[j] == union[k]:
                repetido = True
        if not repetido:
            union.append(array2[j])

    print(f"La unión de los dos arrays es: {union}")

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
union_arrays(a, b)