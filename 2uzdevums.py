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
def koks(viens, divi, trīs):
  sum= viens + divi + trīs
  sum2= sum**2
  return sum2

print('%.2f' % koks(1,2,3))
print('%.2f' %koks(2,4,6))