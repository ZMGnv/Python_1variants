"""
Uzrakstiet Python programmu, lai iegūtu 
starpību starp ievadīto skaitli un 17.
Ja skaitlis ir lielāks par 17, iegūstiet absolūtās starpības dubultu.
"""

sk1=float(input("ievadi skaitli:"))
summa=sk1-17
if summa>17:
    print(2*summa)
print(summa)