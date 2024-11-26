impar = []
par = []
suma_par = 0
suma_impar = 0

for i in [1,4,5,67,34,55,78,90,2,44,65,33,35,50]:
    if i % 2 == 0:
        par.append(i)
        suma_par += i
    else:
        impar.append(i)
        suma_impar += i
print(f"Numeros pares: {par}, suma total: {suma_par}")
print(f"Numeros impares: {impar}, suma total: {suma_impar}")