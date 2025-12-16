time = 18000
for x in range(0, -101, -1):
    y = -1 * (10_000 - x ** 2)**0.5
    ch_4 = int(1500 + x)  # вправовлево
    ch_3 = int(1500 + y)  # вперёдназад
    for _ in range(time):
        pass
    print(ch_4, ch_3)

print('██████████')

for x in range(-100, 1):
    y = (10_000 - x ** 2) ** 0.5
    ch_4 = int(1500 + x)  # вправовлево
    ch_3 = int(1500 + y)  # вперёдназад
    for _ in range(time):
        pass
    print(ch_4, ch_3)

print('██████████')

for x in range(0, 101):
    y = (10_000 - x ** 2) ** 0.5
    ch_4 = int(1500 + x)  # вправовлево
    ch_3 = int(1500 + y)  # вперёдназад
    for _ in range(time):
        pass
    print(ch_4, ch_3)

print('██████████')

for x in range(100, -1, -1):
    y = -1 * (10_000 - x ** 2) ** 0.5
    ch_4 = int(1500 + x)  # вправовлево
    ch_3 = int(1500 + y)  # вперёдназад
    for _ in range(time):
        pass
    print(ch_4, ch_3)