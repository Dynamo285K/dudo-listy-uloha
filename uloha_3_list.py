def sucin(vstup):
    x = 1
    if type(vstup) == list:
        for i in range(len(vstup)):
            x *= vstup[i]
    else:
        print("1")
    return x
    print(x)

c = [2, 3, 5, 7, 11]
print(sucin(c))
sucin(list(range(1, 11)))
sucin([2] * 20)



