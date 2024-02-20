import matplotlib.pyplot as plt

plt.style.use("ggplot")
plt.figure(figsize=(10,5))
plt.plot(dag, vind, zorder=2)
plt.axhline(y=0, color="black", zorder=1)
plt.title("Gjennomsnittsvind vær dag i 2023")
plt.xlabel("Dag")
plt.ylabel("Vindstyrke")
plt.grid()
plt.show()
