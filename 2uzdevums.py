"""
    Funkcija koks akceptē trīs argumentus - skaiļus viens, divi un trīs, 
    aprēķina to summas kvadrātu un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, 
    parādot skaitli ar diviem simboliem aiz komata.

    Argumenti:
        viens {int vai float} -- pirmais skaitlis
        divi {int vai float} -- otrais skaitlis
        tris {int vai float} -- trešais skaitlis
    Atgriež:
        int vai float -- argumentu summa
"""
def koks (sk1, sk2, sk3):
  summa=(sk1+sk2+sk3)**2
  return summa

pirmais=int(input("ievadi 1.skaitli:"))
otrais=int(input("ievadi 2.skaitli:"))
tresais=int(input("ievadi 3.skaitli:"))

tak=koks(pirmais,otrais,tresais)

print("{0:.2f}".format(tak))
