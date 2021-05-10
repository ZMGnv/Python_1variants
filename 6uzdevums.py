"""
Uzrakstiet programmu Python, lai parādītu pašreizējo datumu un laiku.
"""

import datetime
now = datetime.datetime.now()
print ("Pašreizējais datums un laiks : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))