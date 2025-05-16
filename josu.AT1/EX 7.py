n = int(input("Número ímpar: "))

if n % 2 == 0:
    print("Não é ímpar.")
else:
    antes = n - 2
    depois = n + 2
    dif = (antes ** 2) - (depois ** 2)
    print("Diferença:", dif)
