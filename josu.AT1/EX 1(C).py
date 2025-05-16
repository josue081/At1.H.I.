nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

# a. Média Aritmética Simples
media_simples = (nota1 + nota2 + nota3) / 3
print("Média Simples:", media_simples)

# b. Média Ponderada (2, 2, 3)
media_ponderada_1 = (nota1*2 + nota2*2 + nota3*3) / (2 + 2 + 3)
print("Média Ponderada (2,2,3):", media_ponderada_1)

# c. Média Ponderada (1, 2, 2)
media_ponderada_2 = (nota1*1 + nota2*2 + nota3*2) / (1 + 2 + 2)
print("Média Ponderada (1,2,2):", media_ponderada_2)
