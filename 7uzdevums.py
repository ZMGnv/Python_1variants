"""
Uzrakstiet programmu Python, lai aprēķinātu 
trīs ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu, trīskāršojot to.
"""

def summa(x,y,z):
    summa=x+y+z
    if x==y and y==z:
        print((x+y+z)*3)
    else:
        print(x+y+z)

summa(2,2,2)