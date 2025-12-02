rezept = int(input("Welches Rezept möchtest du kochen?, \n (1) Pfannkuchen \n (2) Waffeln \n (3) Käsekuchen \n"))
portionen = int(input("Für wie viele Portionen soll das Rezept sein? "))

if rezept == 1:
    print("Du hast Pfannkuchen gewählt.")
    for x in [str(portionen * 0.5) +" Eier", str(portionen * 50) + "g Mehl", str(portionen *50) + "ml Milch"]:
        print(x)

elif rezept == 2:
    print("Du hast Waffeln gewählt.")
    for x in [str(portionen * 1) +" Eier", str(portionen * 100) + "g Mehl", str(portionen *100) + "ml Milch", str(portionen * 50) + "g Butter"]:
        print(x)

elif rezept == 3:
    print("Du hast Käsekuchen gewählt.")
    for x in [str(portionen * 200) +"g Quark", str(portionen * 100) + "g Zucker", str(portionen * 1) + " Ei", str(portionen * 50) + "g Mehl", str(portionen * 50) + "ml Öl"]:
        print(x)

else:
    print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3.")