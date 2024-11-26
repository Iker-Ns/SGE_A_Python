impar = []
par = []

for i in [1,4,5,67,34,55,78,90,2,44,65,33,35,50]:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")