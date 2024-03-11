import math
a = float(input("Wartość 'a': "))
try: a=math.sqrt(a)
except ValueError: print("ILLEGAL MOVE - NO NEGATIVE ROOTS IN REAL NUMBERS, TOO BAD SONNY")
else: print("Pierwiastek kwadratowy z 'a': "+str(a))
