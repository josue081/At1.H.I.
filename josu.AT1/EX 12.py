print("calculo da média de alunos por turma.")

turmas = int(input("Qual a quantidade de turmas? "))
alunos = int(input("Qual é o total de alunos? "))

media = alunos / turmas

print("Média de alunos por turma:", media)

if media > 40:
    print("Atenção: tem alguma turma com mais de 40 alunos.")
