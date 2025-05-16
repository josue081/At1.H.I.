print("Cálculo do salário com aumento a cada ano.") 

salario = float(input("me diga o seu salário inicial: "))
anos = int(input("Por quantos anos o seu salário aumentou? "))
aumento = float(input("Qual foi o aumento percentual do primeiro ano? "))

for ano in range(anos): 
    salario = salario + (salario * (aumento / 100))
    aumento = aumento * 2

print("Depois de", anos, "anos, o salário será de:", salario) 
