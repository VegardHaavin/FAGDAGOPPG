import csv
import matplotlib.pyplot as plt

filnavn = "ver.csv"
dag=[]
for i in range(1,366):
  dag.append(i)
vind=[]
temp=[]
with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")
  overskrifter = next(filinnhold)
  for rad in filinnhold:
    vind.append(float(rad[4]))
    temp.append(float(rad[3]))


plt.style.use("ggplot")
plt.figure(figsize=(10,5))
plt.plot(dag, vind, zorder=2)
plt.axhline(y=0, color="black", zorder=1)
plt.title("Gjennomsnittsvind vær dag i 2023")
plt.xlabel("Dag")
plt.ylabel("Vindstyrke")
plt.grid()
plt.show()


import matplotlib.pyplot as plt

plt.style.use("ggplot")
plt.figure(figsize=(10,5))
plt.plot(dag, temp, zorder=2)
plt.xlabel("Dag")
plt.title("Gjennomsnittstemperatur vær dag i 2023")
plt.ylabel("Temperatur")
plt.axhline(y=0, color="black", zorder=1)
plt.grid()
plt.show()
