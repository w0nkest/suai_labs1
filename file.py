def raz(s):
    return s.index(max(s)) - s.index(min(s))


print(raz([20, 50, 10, 30, 90, 5]))