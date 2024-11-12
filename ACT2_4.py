cantidad_salario = 12500
iva = 21

if cantidad_salario < 15000:
    iva = 0
elif cantidad_salario < 30000:
    iva = 10

print(f"Iva a pagar {cantidad_salario * iva / 100}")