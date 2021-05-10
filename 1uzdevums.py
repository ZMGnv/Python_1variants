"""
Ir uzrakstīta programma Python.
Summējot divus norādītos veselos skaitļus. 
Tomēr, ja summa ir no 15 līdz 20, tā atgriezīs 20.
IZLABOT programmā pieļautās kļūdas!!!
"""
def summa(x, y):
    summa = x + y
    if summa in range(15, 20):
        return 20
    else:
        return summa

print(summa(10, 6))
print(summa(10, 2))
print(summa(10, 12))