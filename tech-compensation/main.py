import matplotlib.pyplot as plt

map = {
'Amazon': [4836, 164],
'Microsoft': [3210, 159],
'Google': [3037, 192],
'Facebook': [1899, 180],
'Apple': [1166, 175],
'Oracle': [752, 177],
'Salesforce': [743, 175],
'Cisco': [634, 110],
'Uber': [581, 171],
'IBM': [544, 101],
'LinkedIn': [537, 214],
'VMWare': [519, 145],
'Capital One': [488, 108],
'Bloomberg': [478, 177],
'Intel': [396, 125],
'Goldman Sachs': [380, 136],
'JPMorgan Chase': [379, 94],
'Qualcomm': [360, 139],
'PayPal': [311, 134],
'Intuit': [309, 141],
'Twitter': [275, 192],
'Ebay': [256, 126],
'Walmart Labs': [246, 97],
'Adobe': [246, 160],
'Expedia': [227, 134],
'Nvidia': [224, 160],
'Lyft': [220, 218],
'SAP': [209, 112],
'Wayfair': [185, 114],
'Workday': [180, 133],
# Netflix
'Yelp/Dropbox/Atlassian': [168, 178],
'Shopify': [156, 84],
'Visa': [154, 105],
'Yahoo': [153, 132],
'Snap': [152, 195],
'Airbnb': [149, 248],
# 'Yandex': [139, 18],
'Stripe': [137, 226],
'ServiceNow': [133, 107],
'Dell': [132, 86],
'Square': [123, 159],
'ByteDance': [122, 185],
'Splunk': [120, 192],
'EPAM': [110, 64],
'Pinterest': [107, 208],
'Nutanix': [105, 152],
'GM': [104, 76],
}
for i in map:
    if 1 in [c in i for c in {'SAP', 'Atlassian', 'Shopify', 'Yandex', 'ByteDance'}]:
        plt.plot(map[i][0], map[i][1], 'oC2')
    elif 1 in [c in i for c in {'IBM', 'Capital One', 'Bloomberg', 'Goldman Sachs', 'JPMorgan Chase', 'Walmart Labs', 'Wayfair', 'Dell', 'EPAM', "GM"}]:
        plt.plot(map[i][0], map[i][1], 'oC1')
    else:
        plt.plot(map[i][0], map[i][1], 'oC0')
    plt.annotate(i, (map[i][0], map[i][1]))

plt.xlabel('Number of entries')
plt.ylabel('Entry level compensation')
plt.legend([plt.plot([], [], 'o')[0] for i in range(3)],
           ['West coast', 'Rest of USA', 'Rest of World'],
           labelcolor=['C0', 'C1', 'C2'])
plt.show()
