import random

number = random.randint(0,101)

print("Угадайте число от 0 до 100")
while True:
    answer = input("Введите число: ")
    if not number or answer == "exit":
        break
    if not answer.isdigit() or int(answer) < 0 or int(answer) > 100:
        print("Введите правильное число")
        continue

    user_answer = int(answer)
    if user_answer > number:
        print("Загаданное число меньше")
    elif user_answer < number:
        print("Загаданное число больше")
    else:
        print("Молодец! Ты угадал")
        break