#Napíš funkciu sucin(zoznam), ktorá vráti (return) súčin prvkov zoznamu (zoznam obsahuje len čísla).

def sucin(zoznam):
    a = 1
    if len(zoznam) >= 2:

        for i in range(0,len(zoznam)):
            a*=zoznam[i]
    else:
        print("1")
    return a

c = [2, 3, 5, 7, 11]
print(sucin(c))




