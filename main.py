numero = int(input())
primo = True
for i in range(2, round(numero / 2)):
    if numero % i == 0:
        n = int(numero / i)
        print(f"{numero} no es primo, ya que es divisible por {i} ({numero} / {i} = {n})")
        primo = False
        break
if primo:
    print(f"{numero} es primo!")