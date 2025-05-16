dias = int(input("Dias com o carro: "))
km = float(input("KM rodados: "))

custo = dias * 90

if km > 100:
    extra = (km - 100) * 12
else:
    extra = 0

total = custo + extra

print("Total a pagar:", total)
