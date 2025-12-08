def rechner():
    int1 = int(input("Geben Sie die erste Zahl ein: "))
    int2 = int(input("Geben Sie die zweite Zahl ein: ")) 
    int3 = int(input("Geben Sie die dritte Zahl ein: "))
    int4 = int(input("Geben Sie die vierte Zahl ein: ")) 
    int5 = int(input("Geben Sie die fünfte Zahl ein: "))

    summe = int1 + int2 + int3 + int4 + int5

    return summe


ausgabe = rechner()
print("Die Summe der eingegebenen Zahlen ist:", ausgabe)