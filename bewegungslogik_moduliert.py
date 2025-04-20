class Gatter:
    def __init__(self, name, richtung, wert):
        self.name = name
        self.richtung = richtung
        self.wert = wert

    def invertiere_zustand(self):
        self.richtung = "2→1" if self.richtung == "1→2" else "1→2"

    def __str__(self):
        return f"Gatter {self.name} ({self.richtung}), Wert: {self.wert}"


class Zentrum:
    def __init__(self, wert):
        self.wert = wert

    def __str__(self):
        return f"Zentrum C: Zustand neutral, Wert: {self.wert}"


class BewegungslogikModuliert:
    def __init__(self):
        self.gatter_a = Gatter("A", "1→2", 3)
        self.gatter_b = Gatter("B", "2→1", 3)
        self.gatter_c = Zentrum(5)
        self.freie_einheit = 0

    def durchlauf(self, zyklen=20):
        for i in range(1, zyklen + 1):
            print(f"\n--- Zyklus {i} ---")
            print(f"{self.gatter_a.name} ({self.gatter_a.richtung}) überträgt Energie ({self.gatter_a.wert}) zu Zentrum C")
            print(f"{self.gatter_b.name} ({self.gatter_b.richtung}) überträgt Energie ({self.gatter_b.wert}) zu Zentrum C")

            # Modulation der Energie
            if self.gatter_a.richtung == self.gatter_b.richtung:
                self.gatter_c.wert += 2
                print("Modulation: Gleichrichtung → +2 Energie")
            else:
                self.gatter_c.wert += 1
                print("Modulation: Gegenrichtung → +1 Energie")

            if self.gatter_c.wert >= 11:
                print("\nEnergetischer Kollaps (11)! Komprimierung zu 'Baggerschaufeln' [1-1]...\n")
                schaufel_intern = 1
                schaufel_extern = 1
                print("Differenzierte Einheiten [1-1] erzeugt.")
                self.gatter_c.wert = 5
                print("Zentrum C kehrt durch Integration zum Basiswert 5 zurück.")
                self.freie_einheit += schaufel_extern
                print(f"Freie energetische Einheit ({schaufel_extern}) erzeugt (Impulsgeber): {self.freie_einheit}")
                self.gatter_a.invertiere_zustand()
                self.gatter_b.invertiere_zustand()
            else:
                print("Kein Kollaps. Zentrum C stabil.")

            print("Status nach Zyklus:")
            print(f"  {self.gatter_a}")
            print(f"  {self.gatter_b}")
            print(f"  {self.gatter_c}")


if __name__ == "__main__":
    emulator = BewegungslogikModuliert()
    emulator.durchlauf()
