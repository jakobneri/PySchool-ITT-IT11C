def ersetze_vokale(text):
    vokale = "aeiouAEIOU"
    ersatz = "1"
    neuer_text = ""
    
    for buchstabe in text:
        if buchstabe in vokale:
            neuer_text += ersatz
        else:
            neuer_text += buchstabe
            
    return neuer_text

eingabe = input("Bitte einen Text eingeben: ")
ergebnis = ersetze_vokale(eingabe)
print("Text nach dem Ersetzen der Vokale:", ergebnis)