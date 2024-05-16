import random


def description_code(number):
    result = ""
    for i in range(1, (number // 2) + 1):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                result += str(i) + str(j)
    return int(result)


def random_number():
    number = random.randint(3, 20)
    print(f"|{'-'*65}|\n|Случайное число в первом поле: {number}\n|{'-'*65}|")

    return number


print(f"|Пароль к данному числу: {description_code(random_number())}\n|{'-'*65}|")
