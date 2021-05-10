"""
Uzrakstiet programmu Python, lai aprēķinātu 
trīs ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu, trīskāršojot to.
"""
def skaitlu_summa (sk1, sk2, sk3):
  summa =sk1+sk2+sk3
  if sk1 == sk2 == sk3:
      summa = summa * 3
  return summa

sk1=int(input("ievadi pirmo skaitli:"))
sk2=int(input("ievadi otro skaitli:"))
sk3=int(input("ievadi trešo skaitli:"))

print ("summa ir", summa)
