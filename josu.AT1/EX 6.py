primos = []
n = 2

while len(primos) < 100:
    primo = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            primo = False
            break
    if primo:
        primos.append(n)
    n += 1

for p in primos:
    print(p)
