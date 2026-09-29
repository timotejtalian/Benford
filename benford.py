import csv
f = open("data.csv","r")
cislice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
hodnoty = 0

for riadok in csv.reader(f):
    if riadok[0] == "country":
        continue

    if len(riadok) > 5:
        smrt = riadok[5]
        if smrt.isnumeric():
            if int(smrt) != 0:
                prva_cifra = int(str(int(smrt))[0])
                cislice[prva_cifra] += 1
                hodnoty += 1
            else:
                pass
        else:
            pass
    else:
        pass

for cifra in cislice:
    if hodnoty != 0:
        percenta = (cislice[cifra] / hodnoty) * 100
        print(str(round(percenta, 2)) + "%")
    else:
        print("0.00%")


