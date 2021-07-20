procent = int(input('введите число: '))

if procent == 1 or procent == 21:
    print(procent, 'процент', end="/")

elif 1 < procent < 5:
    print(procent, 'процента', end="/")

else:
    print(procent, 'процентов', end="/")