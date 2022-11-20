def vypis_typy(vstup):
    if type(vstup) == list:
        for i in range(0, len(vstup)):
            if type(vstup[i]) == int or vstup[i] == float:
                print(vstup[i], "- číslo")
            elif type(vstup[i]) == str:
                print(vstup[i], "- reťazec")
            else:
                print(vstup[i], "- iný typ")
    else:
        print("toto nie je zoznam")

vypis_typy([12,"x",range(0,5)])
