"""
Uzrakstiet programmu Python, lai aprēķinātu 
trīs ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu, trīskāršojot to.
"""
sk1=float(input("ievadi skaitli:"))
sk2=float(input("ievadi skaitli:"))
sk3=float(input("ievadi skaitli:"))

summa=sk1+sk2+sk3
if sk1==sk2==sk3:
    print(3*summa)
print(summa)