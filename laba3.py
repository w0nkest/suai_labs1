maxlen = ''

for i in input('Введите строку: ').split():
    maxlen = i if len(i) > len(maxlen) else maxlen

print(maxlen)

# доп

string = input('Введите строку: ').split()
maxent, obz = '', input('Введите образец: ')

for s in string:
    maxent = s if s.count(obz) > maxent.count(obz) else maxent

print(maxent)
