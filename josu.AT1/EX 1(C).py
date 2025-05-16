# Agr vai

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

# a. A média aritmética simples
media_simples = (nota1 + nota2 + nota3) / 3
print("Média Simples:", media_simples)

# b. A média ponderada considerando os pesos 2, 2 e 3
media_ponderada_1 = (nota1*2 + nota2*2 + nota3*3) / (2 + 2 + 3)
print("Média Ponderada (2,2,3):", media_ponderada_1)

# c. A média ponderada considerando os pesos 1, 2 e 2 
media_ponderada_2 = (nota1*1 + nota2*2 + nota3*2) / (1 + 2 + 2)
print("Média Ponderada (1,2,2):", media_ponderada_2)
