def description_code(number):
    result = ''
    for i in range(1, (number // 2) + 1):
        for j in range(i+1, number):
            if number % (i + j) == 0:
                result += str(i) + str(j)
    return int(result)


print(description_code(20))
