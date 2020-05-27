revenue = int(input('Введите значение выручки: '))
loss = int(input('Введите значение издержек: '))
if revenue - loss < 0:
    print(f'Убыток компании: {revenue - loss}')
elif revenue - loss > 0:
    print(f'Прибыль компании: {revenue - loss}')
    print(f'Рентабельность выручки: {revenue / loss:.2f}')
    personal = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы на одного сотрудника: {(revenue - loss) / personal:.2f}')
else:
    print(f'Прибыль компании: 0')