def sorting(*args):
    sortedlist = []
    for i in args:
        if len(sortedlist) == 0 or i > sortedlist[-1]:
            sortedlist.append(i)
        elif i < sortedlist[0]:
            sortedlist = [i] + sortedlist
            continue
        elif len(sortedlist) > 0:
            for j in range(1, len(sortedlist)):
                if sortedlist[j-1] <= i <= sortedlist[j]:
                    sortedlist = sortedlist[:j] + [i] + sortedlist[j:]
                    break
    return sortedlist


def maximum(*args):
    return sorting(*args)[-1]


