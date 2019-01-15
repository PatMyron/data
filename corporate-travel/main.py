from collections import OrderedDict
import matplotlib.pyplot as plt
from operator import itemgetter
import requests
import re
# from https://www.businesstravelnews.com/Corporate-Travel-100/2018

s = """Deloitte
IBM
PwC
EY
Apple
McKinsey-Co-
Accenture
Boeing
Microsoft
Lockheed-Martin
Cisco
Amazon
GE
The-World-Bank
ExxonMobil
Google
Bank-of-America
JPMorgan-Chase-Co
KPMG-LLP
Roche
Siemens
BCG
FedEx
Oracle
Johnson-Johnson
Wells-Fargo
Comcast
Citi
DellEMC
Raytheon
Walt-Disney
Facebook
United-Technologies
Sanofi
Northrop-Grumman
Pfizer
DowDuPont
Medtronic
Royal-Dutch-Shell
SAP
Merck
Abbott
AbbVie
Time-Warner
The-Church-of-Jesus-Christ-of-Latter-Day-Saints
Novartis
Nike
General-Motors
GSK
General-Dynamics
Goldman-Sachs
Intel1
International-Monetary-Fund
Toyota-Motor-North-America
Honeywell
Koch
Chevron
UnitedHealth-Group
Walmart
UBS
Credit-Suisse
L3-Technologies
Allergan
Morgan-Stanley
Schlumberger
Bayer
Omnicom-Group
P-G
Epic-Systems
Cognizant
21st-Century-Fox
IPG
Shire
Amgen
Marsh-McLennan-Cos
Airbus-Group
Allstate
Salesforce
BP
PepsiCo
Samsung
Danaher
Stryker
Daimler
ITW
Johnson-Controls
Boston-Scientific
3M
Lilly
Barclays
Coca-Cola
Viacom
Aon
WPP
Verizon
Publicis-Groupe
Deutsche-Bank
Caterpillar
Hewlett-Packard-Enterprise
BAE-Systems"""

volumePerCompany = {}
for line in s.splitlines():
    response = requests.get("https://www.businesstravelnews.com/Corporate-Travel-100/2018/" + line).text
    volumeStrings = [line for line in response.splitlines() if "Volume" in line]
    volumePerCompany[line] = float(re.search("\$(.*?) million", volumeStrings[0]).group(1))

plt.figure(figsize=(8, 15))
plt.barh(*zip(*OrderedDict(sorted(volumePerCompany.items(), key=itemgetter(1))).items()))
plt.xlabel('$M')
plt.title('2017 U.S.-Booked Air Volume')
plt.gca().get_xaxis().get_major_formatter().set_scientific(False)
plt.show()
