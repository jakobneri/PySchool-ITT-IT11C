class car():
    carCounter = 0

    def __init__(self, hersteller, leistung, farbe):
        self.hersteller = hersteller
        self.leistung = leistung
        self.farbe = farbe
        self.Xpos = 5
        self.Ypos = 5
        car.carCounter += 1

    def move(self, x, y):
        self.Xpos += x
        self.Ypos += y

    def position(self):
        return (self.Xpos, self.Ypos)

car1 = car("Toyota", 150, "Rot")
car2 = car("Honda", 130, "Blau")

print(f"Auto 1: {car1.hersteller}, Leistung: {car1.leistung} PS, Farbe: {car1.farbe}")
print(f"Auto 2: {car2.hersteller}, Leistung: {car2.leistung} PS, Farbe: {car2.farbe}")

print(f"Auto 1 Position: {car1.position()}")
print(f"Es gibt insgesamt {car.carCounter} Autos.")