#Napíš funkciu vypis_typy(zoznam)

def vypis_typy(zoznam):
    if type(zoznam) == list:
        for i in range(0,len(zoznam)):
            if type(zoznam[i]) == int:
                print(zoznam[i],"- cislo")
            elif zoznam[i] == float:
                print(zoznam[i], "- cislo")
            elif type(zoznam[i]) == str:
                print(zoznam[i],"- retazec")
            else:
                print(zoznam[i],"- iny typ")
    else:
        print("toto nie je zoznam")

vypis_typy([12, 'x', None, 3.14, [], range(5), '123'])