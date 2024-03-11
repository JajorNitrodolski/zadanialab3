def geoSeq(a=1,b=4,ile=10):
    fact=1
    while ile>0:
        fact*=a*b**(ile-1)
        ile-=1
    return fact
print(geoSeq())