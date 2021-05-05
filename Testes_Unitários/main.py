# TESTES UNITÁRIOS

def teste(n):
    n += 1
    p1 = n % 3
    p2 = (n - 3) % 3
    p3 = (n - 9) % 3
    print(p1, p2, p3)


print(teste(3))
