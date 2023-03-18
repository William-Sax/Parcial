cuentas=3
isabel=[]

i=0
while i<cuentas:
    numeroCuenta=int(input("Digite el numero de cuenta:"))
    #isabel.append(numeroCuenta)
    saldo=int(input(f"Digite el saldo de la cuenta:" ))
    isabel.append(numeroCuenta,saldo)
    i+=1
    print(f"{isabel} \n")
    
isabel.sort()

