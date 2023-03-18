lista = list
contador2=0
contador3=0
multiploAmbos=0
for i  in range(1,10):
    numero=int(input(f"Digite el numero {i}:"))
    if(numero%2==0):
        contador2+=1
    elif(numero%3==0):
        mul3=numero
        contador3+=1
        
    elif(numero%2==0 and numero%3==0):
        ambo=numero
        multiploAmbos+=1
        
print(f"El total de los numeros devisible por 2 es:{contador2}")
print(f"El total de los numeros devisiblepor 3 es:{contador3}")
print(f"El total de los numeros devisible por 2 y 3 es:{multiploAmbos}")