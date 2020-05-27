time = int(input('Введите время в секундах: '))
new_time = f'{time//3600:02d}:{time%3600//60:02d}:{time//3600%60:02d}'
print(new_time)
