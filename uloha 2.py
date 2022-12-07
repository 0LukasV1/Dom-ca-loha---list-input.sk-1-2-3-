#Napíš funkciu nakup(zoznam), ktorá spracuje nákupný zoznam a vráti jeho celkovú cenu.

def nakup(zoznam):
    if type(zoznam) == list:
        a = 0
        b = 0
        for i in range(0,len(zoznam)):

            if i % 2 == 0:
                b=zoznam[i]
            else:
                a += (b*zoznam[i])

        print(a)

    else:
        print("nie je zoznam")

print('cena')
nakup([3, 2.5, 0.5, 10, 1.2, 1.2])
