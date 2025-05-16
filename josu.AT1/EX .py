print("Conversor de tempo: segundos para dias, horas e minutos.")

segundos = int(input("Total de segundos: "))

dias = segundos // 86400
segundos = segundos % 86400

horas = segundos // 3600
segundos = segundos % 3600

minutos = segundos // 60

print("Dias:", dias)
print("Horas:", horas)
print("Minutos:", minutos)
