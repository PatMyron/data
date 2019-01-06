from collections import OrderedDict
import matplotlib.pyplot as plt
from operator import itemgetter
# from https://stores.org/stores-top-retailers-2018/

s = """Walmart	$374.80	Bentonville, Ark.	5,328
Kroger Co.	$115.89	Cincinnati	3,902
Amazon	$102.96	Seattle	456
Costco	$93.08	Issaquah, Wash.	510
Home Depot	$91.91	Atlanta	1,968
Walgreens Boots Alliance	$82.75	Deerfield, Ill.	7,980
CVS Health Corporation	$79.54	Woonsocket, R.I.	9,778
Target	$71.88	Minneapolis	1,822
Lowe's Companies	$63.13	Mooresville, N.C.	1,839
Albertsons Companies	$59.72	Boise, Idaho	2,318
Royal Ahold Delhaize USA	$43.20	Carlisle, Pa.	1,962
Apple Stores / iTunes	$38.60	Cupertino, Calif.	272
Best Buy	$38.59	Richfield, Minn.	1,293
McDonald's	$37.64	Oak Brook, Ill.	14,036
Publix Super Markets	$34.56	Lakeland, Fla.	1,384
TJX Companies	$27.40	Framingham, Mass.	2,983
Aldi	$25.86	Batavia, Ill.	2,250
Macy's	$24.76	Cincinnati	839
Dollar General	$23.47	Goodlettsville, Tenn.	14,534
H-E-B Grocery	$21.94	San Antonio, Texas	330
Dollar Tree	$21.91	Chesapeake, Va.	14,610
Rite Aid	$21.52	Camp Hill, Pa.	2,550
Kohl's	$18.90	Menomonee Falls, Wis.	1,174
Verizon Wireless	$18.89	New York	6,721
YUM! Brands	$17.97	Louisville, Ky.	17,354
Meijer	$17.15	Grand Rapids, Mich.	236
Ace Hardware	$16.62	Oak Brook, Ill.	4,418
Starbucks	$16.53	Seattle	13,930
Wakefern / ShopRite	$16.30	Keasbey, N.J.	360
Nordstrom	$14.77	Seattle	362
Sears Holdings	$14.35	Hoffman Estates, Ill.	944
7-Eleven	$14.33	Dallas	8,094
Ross Stores	$13.99	Pleasanton, Calif.	1,620
Subway	$13.61	Milford, Conn.	25,561
AT&T Wireless	$13.39	Dallas	2,004
Gap	$12.52	San Francisco	2,368
BJ's Wholesale Club	$12.45	Westborough, Mass.	215
J.C. Penney Co.	$12.44	Plano, Texas	866
Bed Bath & Beyond	$12.25	Union, N.J.	1,496
L Brands	$10.99	Columbus, Ohio	2,750
Menard	$10.95	Eau Claire, Wis.	307
Southeastern Grocers	$10.63	Jacksonville, Fla.	735
Health Mart Systems	$10.28	Omaha, Neb.	4,853
Good Neighbor Pharmacy	$9.79	Chesterbrook, Pa.	2,852
Hy-Vee	$9.64	West Des Moines, Iowa	245
AutoZone	$9.48	Memphis, Tenn.	5,399
Alimentation Couche-Tard	$9.30	Tempe, Ariz.	7,195
Wendy's	$9.23	Dublin, Ohio	5,769
Chick-fil-A	$9.10	Atlanta	2,202
Dunkin' Brands Group	$9.06	Canton, Mass.	11,701
Giant Eagle	$9.04	O'Hara Township, Pa.	419
O'Reilly Auto Parts	$9.02	Springfield, Mo.	5,019
Wegmans Food Market	$8.68	Rochester, N.Y.	96
Burger King Worldwide	$8.63	Miami	7,211
Dick's Sporting Goods	$8.60	Coraopolis, Pa.	845
Darden Restaurants	$8.35	Orlando, Fla.	1,765
PetSmart	$8.31	Phoenix	1,466
Sherwin-Williams	$8.03	Cleveland	3,960
Staples	$7.63	Framingham, Mass.	1,185
Army & Air Force Exchange	$7.39	Dallas	946
Bass Pro	$7.34	Springfield, Mo.	181
Tractor Supply Co.	$7.26	Brentwood, Tenn.	1,853
WinCo Foods	$7.12	Boise, Idaho	117
Save-A-Lot	$7.01	Earth City, Mo.	1,292
Ascena Retail Group	$6.61	Suffern, N.Y.	4,728
Dine Brands Global	$6.58	Glendale, Calif.	3,453
Office Depot	$6.38	Boca Raton, Fla.	1,378
GameStop	$6.36	Grapevine, Texas	3,896
Dillard's	$6.12	Little Rock, Ark.	292
Burlington Coat Factory	$5.99	Burlington, N.J.	617
Toys "R" Us	$5.98	Wayne, N.J.	877
Ulta Salon, Cosmetics & Fragrance	$5.88	Bolingbrook, Ill.	1,074
Sephora (LVMH)	$5.87	San Francisco	362
Foot Locker	$5.86	New York	2,174
Ikea North American Svcs.	$5.86	Conshohocken, Pa.	45
Domino's Pizza	$5.77	Ann Arbor, Mich.	5,587
Academy	$5.77	Katy, Texas	243
Panera Bread Company	$5.63	St. Louis, Mo.	2,132
AVB Brandsource	$5.35	Tustin, Calif.	2,953
Signet Jewelers	$5.28	Akron, Ohio	2,966
Big Lots	$5.27	Columbus, Ohio	1,416
Williams-Sonoma	$5.12	San Francisco	607
Saks Fifth Avenue / Lord & Taylor	$5.12	New York	201
Defense Commissary Agency	$5.08	Fort Lee, Va.	238
Hobby Lobby Stores	$4.91	Oklahoma City	844
Speedway	$4.90	Enon, Ohio	2,703
Michaels Stores	$4.86	Irving, Texas	1,236
True Value Co.	$4.80	Chicago	4,311
Discount Tire	$4.72	Scottsdale, Ariz.	975
Sprouts Farmers Market	$4.67	Phoenix	285
Exxon Mobil Corporation	$4.67	Irving, Texas	3,347
Neiman Marcus	$4.57	Dallas	85
Jack in the Box	$4.46	San Diego	2,977
Shell Oil Company	$4.45	Houston	4,656
Sonic	$4.41	Oklahoma City	3,593
Chipotle Mexican Grill	$4.41	Denver	2,371
SUPERVALU	$4.40	Eden Prairie, Minn.	225
Belk	$4.29	Charlotte, N.C.	294
Petco Animal Supplies	$4.17	San Diego	1,502"""

salesPerStore = {}
for line in s.splitlines():
    store = line.split()[-1].replace(',', '')
    sales = [s for s in line.split() if '$' in s][0].strip('$')
    salesPerStore[line.split()[0]] = 1000000000 * float(sales) / float(store)

plt.figure(figsize=(8, 15))
plt.barh(*zip(*OrderedDict(sorted(salesPerStore.items(), key=itemgetter(1))).items()))
plt.xlabel('$')
plt.title('Sales per Store')
plt.gca().get_xaxis().get_major_formatter().set_scientific(False)
plt.show()
