import random

#Списки

empty_list = []
empty_list = list()

none_list = [None] * 10

collections = ['list', 'tuple', 'dict', 'set']

user_data = [
	['Elena', 4.4],
	['Andrey', 4.2]
]

print(len(collections))
print(collections)
collections[3] = 'frozenset'
print(collections)

range_list = list(range(10))
print(range_list)
print(range_list[::2])
print(range_list[::-1])

for idx, collection in enumerate(collections):
	print('#{} {}'.format(idx, collection))

collections.append('OrderedDict')
print(collections)
collections += [None]
del collections[4]
print(collections)

numbers = [4, 17, 19, 9, 2, 6, 10, 13]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

tag_list = ['python', 'course', 'coursera']
print(', '.join(tag_list))

numbers = []
for _ in range(10):
	numbers.append(random.randint(1, 20))
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)
numbers.sort()
print(numbers)

# Кортежи - не изменяемые

empty_tuple = ()
empty_tuple = tuple()

immutables = (int, str, tuple)

blink = ([], [])
blink[0].append(0)
print(blink)

print(hash(tuple()))

one_element_tuple = (1,)
guess_what = (1)
print(type(guess_what))


# Словари


empty_dict = {}
empty_dict = dict()

collections_map = {
	'mutable': ['list', 'set', 'dict'],
	'immutable': ['tuple', 'frozenset']
}

print(collections_map['immutable'])
print(collections_map.get('irresistible', 'not found'))

beatles_map = {
	'Paul': 'Bass',
	'John': 'Guitar',
	'George': 'Guitar'
}
print(beatles_map)
beatles_map['Ringo'] = 'Drums'
print(beatles_map)

del beatles_map['John']
print(beatles_map)

# Добавить новую пару если она не найдена

unknown_dict = {}
print(unknown_dict.setdefault('key', 'default'))
print(unknown_dict)
print(unknown_dict.setdefault('key', 'newdefault'))

print(collections_map)

for key in collections_map:
	print(key)

for key, value in collections_map.items():
	print('{} - {}'.format(key, value))

# OrderedDict - словарь в который добавляется именно в том
# порядке, как положили