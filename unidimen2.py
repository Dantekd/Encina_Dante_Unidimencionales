from unidimen1 import crear_array
def ingresar_vector(cantidad: int) -> list:
    array = crear_array(cantidad)  
    for i in range(cantidad):
        array[i] = int(input(f"Ingrese el número {i+1}: "))
    return array
if __name__ == "__main__":
    numeros = ingresar_vector(3)
    print(numeros)