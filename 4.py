number = int(input('Введите число: '))
a = 0
while number > 0:
    if number % 10 > a:
        a = number % 10
    if a == 9:
        break
    number = number // 10
print(a)
