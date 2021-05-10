"""
Uzrakstiet Python programmu, lai iegūtu 
starpību starp ievadīto skaitli un 17.
Ja skaitlis ir lielāks par 17, iegūstiet absolūtās starpības dubultu.
"""
import math
sk=float(input("Ievadi skaitli"))
if sk<=17:
    rez=sk-17
else:
    rez=(sk-17)*2
print(rez)