def nakup(zoznam):
    cena = 0
    kolko = 0
    if type(zoznam) == list:
        for i in range(len(zoznam)):
            if i % 2 == 0:
                kolko = zoznam[i]
            else:
                cena += (zoznam[i]*kolko)
        print(cena)
    else:
        print('nie je nakupny zoznam')

nakup([3, 2.5, 0.5, 10, 1.2, 1.2])

