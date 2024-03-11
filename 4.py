def rectTria(a,b,c):
    if c**2==a**2+b**2: return True
    return False
a=int(input("Bok 'a': "))
b=int(input("Bok 'b': "))
c=int(input("Bok 'c': "))
print("Trójkąt o bokach 'a', 'b', 'c' jest prostokątny: ",end="")
print(rectTria(a,b,c))