def adder():
    killSwitch = False
    total = 0
    while not killSwitch:
        userInput = input("Bitte eine Zahl eingeben (oder Q zum Beenden): ")
        if userInput == 'Q':
            killSwitch = True
            return total
        else:
                number = int(userInput)
                total += number 
                

result = adder()
print("Ergebnis ist: " + str(result))

