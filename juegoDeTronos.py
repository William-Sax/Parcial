cuentas = []
i= 1

while i <= 10:
    cuenta = {}
    saldo = float(input(f"Ingrese el saldo de la cuenta {i}: "))
    cuenta["i"] = i
    cuenta["saldo"] = saldo
    i = i + 1
    cuentas.append(cuenta)

def ordenar(item):
  return item['saldo']

cuentas.sort(reverse=True, key=ordenar)

print(cuentas)