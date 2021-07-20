duration = int(input('Введите время в секундах: '))

min = duration // 60
hour = duration // 3600
day = duration // 86400
month = duration // (86400 * 31)
year = duration // ((86400 * 31) * 12)

if duration >= 60 and duration < 3600:
    print(f'{min} мин {duration % 60} сек')

elif duration >= 3600 and duration < 86400:
    print(f'{hour} час {min % 60} мин {duration % 60} сек')

elif duration >= 86400 and duration < (86400 * 31):
    print(f'{day} день {hour % 24} час {min % 60} мин {duration % 60} сек')

elif duration >= (86400 * 31) and duration < ((86400 * 31) * 12):
    print(f'{month} месяц {day % 31} день {hour % 24} час {min % 60} мин {duration % 60} сек')

elif duration >= ((86400 * 31) * 12):
    print(f'{year} лет {month % 12} месяц {day % 31} день {hour % 24} час {min % 60} мин {duration % 60} сек')

elif duration < 60 and duration >= 0:
    print(f'{duration} секунд')

elif duration < 0:
    print('Введите целое число в секундах')

# duration = int(input('Введите время в секундах: '))

# sek = duration % 60
# min = duration // 60 % 60
# days = duration // (3600 * 24)
# hours = duration // 3600 % 24

# print('days: ', days, ',', ' hours: ', hours, ',', ' minutes: ', min, ',', ' sekunds: ', sek, '.', sep='')
