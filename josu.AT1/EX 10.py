s = int(input("Segundos: "))

d = s // 86400
s = s % 86400

h = s // 3600
s = s % 3600

m = s // 60
s = s % 60

print(d, "dias,", h, "horas,", m, "minutos e", s, "segundos.")
