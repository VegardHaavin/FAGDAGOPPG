import csv

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