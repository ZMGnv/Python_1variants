"""
Uzrakstiet programmu Python, lai aprēķinātu 
trīs ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu, trīskāršojot to.
"""
sk1=int(input("ievadi pirmo skaitli:"))
sk2=int(input("ievadi otro skaitli:"))
sk3=int(input("ievadi trešo skaitli:"))

if sk1==sk2==sk3: 
  print((sk1*sk2*sk3)*3)

else:
  print (sk1+sk2+sk3)

  