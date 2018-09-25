# Найти медиану списка
import random
import statistics

numbers = []
numbers_size = random.randint(10, 15)

for _ in range(numbers_size):
	numbers.append(random.randint(10, 20))

print(numbers)

numbers.sort()
print(numbers)

half_size = len(numbers) // 2
median = None

if numbers_size % 2 == 1:
	median = numbers[half_size]
else:
	median = sum(numbers[half_size-1:half_size+1]) / 2

print(median)
print(statistics.median(numbers))



# Словари

empty_dict = {}
empty_dict = dict()

collections_map = {
	'mutable': ['list', 'set', 'dict'],
	'immutable': ['tuple', 'frozenset']
}

print(collections_map['immutable'])
print(collections_map.get('irresistible', 'not found'))
print('mutable' in collections_map)

beatles_map = {
	'Paul': 'Bass',
	'John': 'Guitar',
	'George': 'Guitar',
}
print(beatles_map)

beatles_map['Ringo'] = 'Drums'
print(beatles_map)

del beatles_map['John']
print(beatles_map)

#Добавляем значения, если они не найдены в словаре
unknown_dict = {}
print(unknown_dict.setdefault('key', 'default'))
print(unknown_dict)

for key in collections_map:
	print(key)

for key, value in collections_map.items():
	print('{} - {}'.format(key, value))