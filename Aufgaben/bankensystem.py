class konto():
    konten = 0

    def __init__(self, inhaber, kontonummer, kontostand=0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        konto.konten += 1
    def einzahlen(self, betrag):
        self.kontostand += betrag

    def abheben(self, betrag):
        if betrag <= self.kontostand:
            self.kontostand -= betrag

    def anzeigen(self):
        return self.kontostand
    
konto1 = konto("Alice", "DE1234567890", 1000)
print(konto1.anzeigen())
konto1.einzahlen(500)
print(konto1.anzeigen())
konto1.abheben(300)
print(konto1.anzeigen())
konto2 = konto("Bob", "DE0987654321")
print(konto2.anzeigen())
print("Anzahl der Konten:", konto.konten)
