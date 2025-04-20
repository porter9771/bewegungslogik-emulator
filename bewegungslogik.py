class XGatter:
    def __init__(self, name, zustand, wert):
        self.name = name
        self.zustand = zustand
        self.wert = wert

    def energie_uebertragen(self, ziel_gatter):
        print(f"{self.name} ({self.zustand}) überträgt Energie ({self.wert}) zu {ziel_gatter.name}")
        ziel_gatter.wert += self.wert

    def invertiere_zustand(self):
        if self.zustand == "1→2":
            self.zustand = "2→1"
        elif self.zustand == "2→1":
            self.zustand = "1→2"
        print(f"{self.name} invertiert Zustand zu {self.zustand}")


class BewegungslogikEmulator:
    def __init__(self):
        self.gatter_a = XGatter("Gatter A", "1→2", 3)
        self.gatter_b = XGatter("Gatter B", "2→1", 3)
        self.gatter_c = XGatter("Zentrum C", "neutral", 5)
        self.freie_einheit = 0

    def zyklus(self):
        self.gatter_a.energie_uebertragen(self.gatter_c)
        self.gatter_b.energie_uebertragen(self.gatter_c)

        if self.gatter_c.wert == 11:
            print("\nEnergetischer Kollaps! Zustand 11 erreicht.\n")
            self.gatter_c.wert = 5
            self.freie_einheit += 1
            print(f"Freie energetische Einheit erzeugt (Impulsgeber): {self.freie_einheit}")
            self.gatter_a.invertiere_zustand()
            self.gatter_b.invertiere_zustand()

        print("Status nach Zyklus:")
        print(f"  {self.gatter_a.name}: {self.gatter_a.zustand}, Wert: {self.gatter_a.wert}")
        print(f"  {self.gatter_b.name}: {self.gatter_b.zustand}, Wert: {self.gatter_b.wert}")
        print(f"  {self.gatter_c.name}: Zustand neutral, Wert: {self.gatter_c.wert}\n")


def starte_emulation(zyklen=5):
    emulator = BewegungslogikEmulator()
    for zyklus in range(zyklen):
        print(f"\n--- Zyklus {zyklus + 1} ---")
        emulator.zyklus()


if __name__ == "__main__":
    starte_emulation(10)
