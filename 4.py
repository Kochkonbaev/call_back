# дополните генератор словарей, чтобы получить календарь
# import pandas


week = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'thursday',
    'Friday',
    'Saturday',
    'Sunday'
    )

day = [
    [1, 8, 15, 22],
    [2, 9, 16, 23],
    [3, 10, 17, 24],
    [4, 11, 18, 25],
    [5, 12, 19, 26],
    [6, 13, 20, 27],
    [7, 14, 21, 28]
    ]

# cal = {x: y for x, y in zip(week, day)}
#
# df = pandas.DataFrame(cal)
#
# print(df)

# превратите код в функцию, которая принимает кортеж и список


def calc(a, b):
    cal = {x: y for x, y in zip(a, b)}
    return cal


calc(week, day)

print(calc(week, day))
