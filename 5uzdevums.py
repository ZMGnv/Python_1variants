"""
Uzrakstiet Python programmu, lai iegūtu 
starpību starp ievadīto skaitli un 17.
Ja skaitlis ir lielāks par 17, iegūstiet absolūtās starpības dubultu.
"""

def starpibaa(x):
    if x <= 17:
        return 17-x
    else:
        return (x-17)*2

x=int(input("ievadi skaitli:"))
print("starpība ir ", starpibaa(x))
