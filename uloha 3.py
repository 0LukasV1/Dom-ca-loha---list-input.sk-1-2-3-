#Napíš funkciu sucin(zoznam), ktorá vráti (return) súčin prvkov zoznamu (zoznam obsahuje len čísla).

def vypis_typy(zoznam):
    if type(zoznam) == list:
        for i in range(0,len(zoznam)):
            if type(zoznam[i]) == int or zoznam[i] == float:
                print(zoznam[i],"- číslo")
            elif type(zoznam[i]) == str:
                print(zoznam[i],"- reťazec")
            else:
                print(zoznam[i],"- iný typ")
    else:
        print("toto nie je zoznam")

vypis_typy([12,"x",range(0,5)])