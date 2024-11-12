num1, num2 = 10, 10

message = "igual a"

if num1 > num2:
    message = "mas grande que"
elif num1 < num2:
    message = "mas pequeño que"

print(f"{num1} es {message} {num2}")