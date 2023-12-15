class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        else:
            self.state = "doručen"
            return "Doručení uloženo"


class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state} cena {self.value}."


class ValuablePackage(Package):
    def __init__(self, address, weight, value, state="nedoručen. "):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() +  f"Balík má hodnotu hodnotu {self.value} Kč."

# Vytvoření objektů
valuable_package = ValuablePackage("Václavské Náměstí 12, Praha", 0.25, 5000)
package = Package("Jiřího z Poděbrad 9, Brno", 1.5, "doručen")

# Výpis informací o balících
print(valuable_package)
print(package)

# Vytvoření objektů
package1 = Package("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
package2 = Package("Jiřího z Poděbrad 9, Brno", 1.5, "doručen")
package3 = ValuablePackage("Lidická 364, Pardubice", 2, "doručen", 350)

# Výpis informací o balících
print(package1)
print(package2)

# Zkouška metody deliver
print(package1.deliver())
print(package1)  # Balík by měl být nyní ve stavu "doručen"
print(package1.deliver())  # Metoda by nyní měla vrátit zprávu, že balík již byl doručen
print(package3)

print(package1)

class Ticket:
    def __init__(self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number


class TrainTicket(Ticket):
    def __init__(self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class

    def get_price(self):
        if self.fare_class == 'economy':
            return self.basic_price
        elif self.fare_class == 'business':
            return self.basic_price * 1.2


class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages

    def get_price(self):
        luggage_price = self.checkout_luggages * 2000
        if self.fare_class == 'economy':
            return self.basic_price + luggage_price
        elif self.fare_class == 'business':
            return self.basic_price * 1.5 + luggage_price