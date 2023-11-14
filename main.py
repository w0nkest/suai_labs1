import laba4

nums = []

for i in range(4):
    while 1:
        try:
            n = float(input('Введите число: '))
        except:
            n = 10**10
        if n != 10**10:
            break
        print('Это не число')
    nums.append(n)

print(laba4.maximum(*nums))

# доп

newnums = []

while 1:
    nums = input('Введите числа, элементы не являющиеся числами будут удалены: ').split()
    for i in nums:
        try:
            i = float(i)
        except:
            continue
        newnums.append(i)
    if len(newnums) == 0:
        print('Вы не ввели ни одного числа, повторите попытку')
    else:
        break

print(laba4.maximum(*newnums))
