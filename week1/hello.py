print("Hello, World")
for i in range(4):
    print(i)

num = 13
print (type(num))
num = float(num)
print (num)
print(100 % 1)

year = 2020
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) #проверяем високосный год
print (is_leap)

example_string = "Курс про Python на Courcera"
print(example_string[9:])
example_string = "0123456789" #берем каждую вторую цифру, т.е только четные
print(example_string[::2])
example_string = "Привет, Москва"
print(example_string[::-1]) #разворачиваем строку
example_string = "Считаем количество буквы о в строке" #именно русскую о
print(example_string.count("о"))
example_string = "2017"
print(example_string.isdigit())
print("3.14" in "Число Пи = 3.1415926") #проверяем вхождение подстроки в строку

print("{} не лгут, но {} пользуются формулами. ({})".format(
	"Цифры", "Лжецы", "Robert A.Heinlein"))
subject = "оптимизация"
author = "Donald Knuth"
print(f"Преждевременная {subject} - корень всех зол. ({author})")

num = 8
print(f"Binary: {num:#b}")

num = 2/3
print(f"{num:.3f}")
''' Ввод имени
name = input("Введите ваше имя: ")
print(f"Привет, {name}")
'''
example_bytes = b"Hello"
print(type(example_bytes))
print(example_bytes)
for element in example_bytes:
	print(element)

example_string = "привет"
print(type(example_string))
print(example_string)
encoding_string = example_string.encode(encoding="utf-8")
print(encoding_string)
print(type(encoding_string))
decoded_string = encoding_string.decode()
print(decoded_string)

answer = None

result = 0 
for i in range(101): #сумма от 0 до 100
	result += i
print(result)
result = 0
for i in range (2, 5): #от 2 до 6
	print(i)
print()
for i in range (1, 10, 2): #идем от 1 до 9 с шагом 2
	print(i)

print(f"string")

print(r"//\\")