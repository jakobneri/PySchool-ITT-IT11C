stundenlohn = float(input("Geben Sie Ihren Stundenlohn in Euro ein: "))
tag = 8
monat = 22
jahr = 12
stop = input('Drücken Sie die Eingabetaste zum Ausgeben...')


tagesgehalt = stundenlohn * tag
monatsgehalt = tagesgehalt  * monat
jahresgehalt = monatsgehalt * jahr
tagesgehaltNetto = tagesgehalt * 0.7
monatsgehaltNetto = monatsgehalt * 0.7
jahresgehaltNetto = jahresgehalt * 0.7

print("Ihr Tagesgehalt beträgt: ", tagesgehalt, "Euro brutto"," / ", tagesgehaltNetto, "Euro netto")
print("Ihr Monatsgehalt beträgt: ", monatsgehalt, "Euro brutto", " / ", monatsgehaltNetto, "Euro netto")
print("Ihr Jahresgehalt beträgt: ", jahresgehalt, "Euro brutto", " / ", jahresgehaltNetto, "Euro netto")

stop