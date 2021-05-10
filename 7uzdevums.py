"""
Uzrakstiet programmu Python, lai aprēķinātu 
trīs ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu, trīskāršojot to.
"""
a=float(input("Ievadi skaitli a:"))
b=float(input("Ievadi skaitli b:"))
c=float(input("Ievadi skaitli c:"))
if a==b and b==c:
    sum=(a+b+c)*3
else:
    sum=(a+b+c)
print(sum)