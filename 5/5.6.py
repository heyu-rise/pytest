import math

knights = {'ssssss': 'sdagsdf', 'gasdfasf': 'hhhhhhh'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['wwww', 'dsafasd', 'fasdfav']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
x = list(zip(questions, answers))
print(x)
for i, j in reversed(list(zip(questions, answers))):
    print('What is your {0}?  It is {1}.'.format(i, j))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for v in raw_data:
    print(v)
    if not math.isnan(v):
        filtered_data.append(v)
print(filtered_data)
