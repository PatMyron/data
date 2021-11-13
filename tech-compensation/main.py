import matplotlib.pyplot as plt

map = {
    'Amazon': [4836, 164, 3.8],
    'Microsoft': [3210, 159, 4.4],
    'Google': [3037, 192, 4.5],
    'Facebook': [1899, 180, 4.3],
    'Apple': [1166, 175, 4.3],
    'Oracle': [752, 177, 3.8],
    'Salesforce': [743, 175, 4.4],
    'Cisco': [634, 110, 4.3],
    'Uber': [581, 171, 4.1],
    'IBM': [544, 101, 4],
    'LinkedIn': [537, 214, 4.4],
    'VMWare': [519, 145, 4.3],
    'Capital One': [488, 108, 4.2],
    'Bloomberg': [478, 177, 4.1],
    'Intel': [396, 125, 4.2],
    'Goldman Sachs': [380, 136, 4],
    'JPMorgan Chase': [379, 94, 4],
    'Qualcomm': [360, 139, 4.2],
    'PayPal': [311, 134, 4.1],
    'Intuit': [309, 141, 4.5],
    'Twitter': [275, 192, 4.2],
    'Ebay': [256, 126, 4.1],
    'Walmart Labs': [246, 97, 2.9],
    'Adobe': [246, 160, 4.5],
    'Expedia': [227, 134, 4.1],
    'Nvidia': [224, 160, 4.7],
    'Lyft': [220, 218, 3.9],
    'SAP': [209, 112, 4.5],
    'Wayfair': [185, 114, 3.4],
    'Workday': [180, 133, 4.2],
    # 'Netflix': [176, 511],
    'Yelp/Dropbox/Atlassian': [168, 178], # 3.5, 4.3, 4.6
    'Shopify': [156, 84, 4.3],
    'Visa': [154, 105, 4],
    'Yahoo': [153, 132, 4.1],
    'Snap': [152, 195, 4],
    'Airbnb': [149, 248, 4.4],
    # 'Yandex': [139, 18],
    'Stripe': [137, 226, 4.1],
    'ServiceNow': [133, 107, 4.4],
    'Dell': [132, 86, 4.2],
    'Square': [123, 159, 4.2],
    'ByteDance': [122, 185, 4.3],
    'Splunk': [120, 192, 4.1],
    'EPAM': [110, 64, 4.2],
    'Pinterest': [107, 208, 4.2],
    'Nutanix': [105, 152, 4.1],
    'GM': [104, 76, 4],
    'Indeed': [102, 134, 4.4],
    'Accenture': [102, 123, 4.1],
    'Tesla': [100, 130, 3.7],
    'Comcast': [100, 89, 3.8],
    'Zillow': [99, 165, 4.3],
    'Qualtrics': [94, 139, 4.2],
    'GoDaddy': [94, 126, 4.1],
    'DoorDash': [90, 196, 3.9],
    'Spotify': [87, 144, 4.1],
    'MS': [86, 107, 4],
    'Cerner': [85, 71, 3.7],
}
entries, comp = 0, 0
for i in map:
    entries += map[i][0]
    comp += map[i][0] * map[i][1]
    if 1 in [c in i for c in {'SAP', 'Atlassian', 'Shopify', 'Yandex', 'ByteDance', 'Spotify'}]:
        plt.plot(map[i][0], map[i][1], 'oC2')
    elif 1 in [c in i for c in {'IBM', 'Capital One', 'Bloomberg', 'Goldman Sachs', 'JPMorgan Chase', 'Walmart Labs', 'Wayfair', 'Dell', 'EPAM', 'GM', 'Indeed', 'Accenture', 'Comcast', 'Qualtrics', 'GoDaddy', 'MS', 'Cerner'}]:
        plt.plot(map[i][0], map[i][1], 'oC1')
    else:
        plt.plot(map[i][0], map[i][1], 'oC0')
    plt.annotate(i, (map[i][0], map[i][1]))
print(entries)
print(comp / entries)
plt.xlabel('Number of entries')
plt.ylabel('Entry level compensation')
plt.legend([plt.plot([], [], 'o')[0] for i in range(3)],
           ['West coast', 'Rest of USA', 'Rest of World'],
           labelcolor=['C0', 'C1', 'C2'])
plt.show()
