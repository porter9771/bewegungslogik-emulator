import matplotlib.pyplot as plt

zyklen = 20
werte_c = []
impulse = []

# Startwerte
wert_a = 3
wert_b = 3
wert_c = 5
zustand_a = "1→2"
zustand_b = "2→1"

# Bewegungslogische Modulation:
# Gleichrichtung (A == B): mehr Energiefluss
# Gegenrichtung: geringerer Energiefluss
for i in range(zyklen):
    if zustand_a == zustand_b:
        wert_c += 2
    else:
        wert_c += 1

    werte_c.append(wert_c)

    if wert_c >= 11:
        impulse.append(1)
        wert_c = 5
        zustand_a = "2→1" if zustand_a == "1→2" else "1→2"
        zustand_b = "1→2" if zustand_b == "2→1" else "2→1"
    else:
        impulse.append(0)

# Plot erzeugen
plt.figure(figsize=(12, 6))
plt.plot(range(zyklen), werte_c, label='Zentrum C – Frequenzverlauf', color='blue', marker='o', linewidth=2)

for i, imp in enumerate(impulse):
    if imp == 1:
        plt.axvline(x=i, color='red', linestyle='--', alpha=0.6)
        plt.plot(i, werte_c[i], 'ro')
        plt.text(i, werte_c[i] + 0.3, '⚡', ha='center', fontsize=12)

plt.title("Frequenzvisualisierung – Bewegungslogik")
plt.xlabel("Zyklus")
plt.ylabel("Energie in Zentrum C")
plt.ylim(5, 15)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
