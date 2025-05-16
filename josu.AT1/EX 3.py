valor = float(input("Valor da compra: "))

if valor <= 500:
    imposto = 0
else:
    imposto = (valor - 500) * 0.5

print("Imposto:", imposto)
