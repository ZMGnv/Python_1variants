"""
Uzrakstiet Python programmu, lai iegūtu 
starpību starp ievadīto skaitli un 17.
Ja skaitlis ir lielāks par 17, iegūstiet absolūtās starpības dubultu.
"""

skaitlis= float(input('ievadi skaitli: '))

if skaitlis <= 17:
    rez=abs(skaitlis-17)
else:
    starp=abs(skaitlis-17)
    rez=starp*2

print(rez)