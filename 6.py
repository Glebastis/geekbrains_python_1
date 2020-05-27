first_result = int(input('Введите результат спортсмена в первый день: '))
aim_result = int(input('Введите желаемый результат спортсмена: '))
day = 1
while first_result <= aim_result:
    first_result *= 1.1
    day += 1
print(day)