liste = [ 1, 2, 3, "Hallo", 5, "Du Hurensohn", 7, 8, 9, 10 ]
num1 = 3
num2 = 7

def listenteil(liste, num1, num2):
    ausgabe = []
    for objekt in liste:
        if liste.index(objekt) >= num1 and liste.index(objekt) <= num2:
            ausgabe.append(objekt)
    return ausgabe 



ausgabe = listenteil(liste, num1, num2)
print ("Der ausgewählte Listenteil ist:", ausgabe)