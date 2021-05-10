"""
Uzrakstiet programmu Python, lai parādītu 
pirmās un pēdējās krāsas no šī saraksta.

krasa_saraksts = ["sarkans", "zaļš", "balts", "melns"]
"""
krasa_saraksts = ["sarkans", "zaļš", "balts", "melns"]
x=0
y=len(krasa_saraksts)-1
for i in [x, y]:
    print(krasa_saraksts[i])