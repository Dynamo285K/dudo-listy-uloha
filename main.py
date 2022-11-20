def ret(vstup):
    if type(vstup) == list:
        for i in range(0, len(vstup)):
            if type(vstup[i]) == int or vstup[i] == float:
                print(vstup[i], "je cislo")
            elif type(vstup[i]) == str:
                print(vstup[i], "je string")
            else:
                print(vstup[i], "iny typ")
    else:
        print("nie je list")



ret([12, 'x', None, 3.14, [], range(5), '123'])

