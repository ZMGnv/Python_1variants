"""
Uzrakstiet programmu Python, lai dotajā sarakstā saskaitītu 
cik skaitļi 4 ir  dotajā sarakstā.
  """
skaitļi = ["4", "5", "6", "4", "7", "8", "4"]
i=0
x=len(skaitļi)-1
sk=0
while i<=x:
  if skaitļi[i]=="4":
    sk= sk + 1
    i= i+1
  else:
    i= i+1
print(sk)