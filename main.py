def encontrar_mayor(numeros):
   
    mayor = numeros[0]
    for num in numeros[1:]:
        if num > mayor:
            mayor = num
    return mayor
print("Ingresa cinco números:")
numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)
mayor = encontrar_mayor(numeros)
print("El número más grande es:", mayor)