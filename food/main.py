import matplotlib.pyplot as plt

fruit = {
    'banana': [.45, 7, '🍌'],
    'apple': [.9, 50, '🍎'],
    'strawberry/blueberry': [1.5, 7, '🍓/🫐'],
    'grape': [1.3, 7, '🍇'],
    'orange': [.75, 50, '🍊'],
    'watermelon': [.3, 7, '🍉'],
    'lemon': [2, 50, '🍋'],
    'peach/avocado': [1, 7, '🍑/🥑'],
    'pineapple': [1.4, 7, '🍍'],
    'cherry': [1.7, 7, '🍒'],
    'cantaloupe': [.6, 11, '🍈'],
    'pear': [.9, 10, '🍐'],
    'lime': [1.5, 50],
    'raspberry/blackberry': [4, 3],
    'clementine': [1.1, 11, '🍊'],
    'plum': [1.2, 4],
    'nectarine': [1, 4, '🍑'],
    'mango': [.8, 12, '🥭'],
}
for i in fruit:
    plt.plot(fruit[i][1], fruit[i][0], 'oC0')
    plt.annotate(i, (fruit[i][1], fruit[i][0]))
veg = {
    'potato': [.3, 100, '🥔'],
    'tomato': [1.2, 14, '🍅'],
    'onion': [.5, 150, '🧅'],
    'carrot': [.5, 30, '🥕'],
    'lettuce': [1, 7, '🥬'],
    'bell pepper/cauliflower': [1.1, 14, '🫑'],
    'broccoli': [.9, 10, '🥦'],
    'cucumber': [.75, 7, '🥒'],
    'celery': [.8, 25],
    'salad/mushroom': [3, 7, '🥗/🍄'],
    'corn': [.9, 7, '🌽'],
    'garlic': [2, 150, '🧄'],
    'spinach': [1.4, 7],
    'green bean': [1.1, 7, '🫛'],
    'sweet potato': [.6, 90, '🍠'],
    'green onion': [1.2, 7],
    'cabbage': [.3, 30, '🥬'],
    'asparagus': [1.7, 7],
}
for i in veg:
    plt.plot(veg[i][1], veg[i][0], 'oC2')
    plt.annotate(i, (veg[i][1], veg[i][0]))
plt.xlabel('Days to expire')
plt.ylabel('USD / pound')
plt.legend([plt.plot([], [], 'o')[0], plt.plot([], [], 'oC2')[0]],
           ['Fruit', 'Vegetable'],
           labelcolor="markerfacecolor")
plt.show()
