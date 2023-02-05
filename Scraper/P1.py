from random import randint
line = "2 2 55 5 622 3"
a = list(map(int, line.split(' ')))
for i in a:
    print(i, end=' ')
print()

while True:
    a = randint(0, 100)
    print(a)
    if a >= 80:
        break

days = ["MONDAY", "TUESDAY", "WEDNESDAY",
        "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

for i in days:
    print(i.upper(), end=' ')
    print(i.lower(), end=' ')
    print(i.capitalize(), end=' ')
    print(i.replace("DAY", ""), end=' ')
    print(i[0:3], end=' ')
    print(i.count("E"), end=' ')
    print()
print()
