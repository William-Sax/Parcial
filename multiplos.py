cantidad = 20

multiplo2   = 0
multiplo3   = 0
multiplo23   = 0

i = 0

while i < cantidad:
    numero = int(input(f"Ingrese el número {i+1}:"))
    i += 1
    if  numero%2 == 0:
        multiplo2+=1
    elif numero%3== 0:
        multiplo3+=1
    elif numero%3 == 0 and numero%2:
        multiplo23 +=1

print(f"Los multiplos de 2 son: {multiplo2}")
print(f"Los multiplos de 3 son: {multiplo3}")
print(f"Los multiplos de 2 y de 3 son: {multiplo23}")