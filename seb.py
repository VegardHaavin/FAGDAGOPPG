
import matplotlib.pyplot as plt

plt.style.use("ggplot")
plt.figure(figsize=(10,5))
plt.plot(dag, temp, zorder=2)
plt.axhline(y=0, color="black", zorder=1)
plt.title("Gjennomsnittstemperatur vær dag i 2023")
plt.xlabel("Dag")
plt.ylabel("Temperatur")
plt.grid()
plt.show()
