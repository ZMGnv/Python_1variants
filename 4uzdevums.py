"""
Uzrakstiet programmu Python, lai dotajā sarakstā saskaitītu 
cik skaitļi 4 ir  dotajā sarakstā.
  """
def saraksts(sarak):
  count = 0  
  for sarak in sarak:
    if sarak == 4:
      count = count + 1

  return count
print("Dotajā sarakstā ir ", saraksts([8, 4, 3, 4, 5, 7, 2, 6, 4, 4, 8, 4]), "skaitļi 4")