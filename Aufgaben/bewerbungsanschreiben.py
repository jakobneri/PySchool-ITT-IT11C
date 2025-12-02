name = input('Was ist ihr Name? ')
birthyear = input('In welchem Jahr sind Sie geboren? ')
birthyear = int(birthyear)
currentyear = 2025
place  = input('Wo wohnen Sie? ')
recipientName = input('Wie ist der Name des Empfängers? ')
recipientGenderMale = input('Ist der Empfänger männlich? (ja/nein) ').lower() == 'ja'
stop = input('Drücken Sie die Eingabetaste zum Ausgeben...')

print('\nBewerbungsanschreiben\n')
if recipientGenderMale:
    print('Sehr geehrter Herr ' + recipientName + ',')
else:
    print('Sehr geehrte Frau ' + recipientName + ',')
print('Mein Name ist ' + name)
print('Ich bin '+ str(birthyear) + ' geboren und ' + str(currentyear - birthyear) + ' Jahre alt')
print('Ich komme aus ' + place)

stop