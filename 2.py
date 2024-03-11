import random
lista1=[]
for i in range(0,10):
    lista1.append(random.randint(1,1000))
listaNowa=[x for x in lista1 if x%2==0]
print(listaNowa)