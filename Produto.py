def ehprimo():
    primo = 0
    for i in x:
        for j in range(1, i+1):
            if i > 0 and i % j == 0:
                primo += j
        if primo == i+1:
            primos.append(i)
        primo = 0


def mult():
    produto = 'SEM PRODUTO'
    if len(primos) == 4:
        produto = 1
        for i in primos:
            produto *= i
    return produto


x = [int(p) for p in input().split()]
primos = []
ehprimo()
print(mult())
