import math
import matplotlib.pyplot as plt

w, h = 2, 19

values = [[0 for x in range(w)] for k in range(h)]
abweichung = [[0 for x in range(w+1)] for k in range(h)]

values[0][0] = -5
values[0][1] = 3
values[1][0] = -4
values[1][1] = 2.5
values[2][0] = -3
values[2][1] = 2
values[3][0] = -2
values[3][1] = 1.5
values[4][0] = -1
values[4][1] = 1
values[5][0] = 0
values[5][1] = 0.5
values[6][0] = -4.5
values[6][1] = 2.75
values[7][0] = -3.5
values[7][1] = 2.1
values[8][0] = -2.5
values[8][1] = 1.85
values[9][0] = -2.1
values[9][1] = 1.66
values[10][0] = -1.5
values[10][1] = 1.45
values[11][0] = -4.75
values[11][1] = 2.8
values[12][0] = -4.25
values[12][1] = 2.4
values[13][0] = -2.8
values[13][1] = 1.49
values[14][0] = -1.2
values[14][1] = 1.1
values[15][0] = -0.5
values[15][1] = 0.75
values[16][0] = -0.85
values[16][1] = 0.95
values[17][0] = -0.1
values[17][1] = 0.55
values[18][0] = -3.8
values[18][1] = 1.9

print(values)

# Mittelwert berechnen
sum = 0

for y in range(h):
    sum += values[y][0]

mittel_x = sum / h


sum = 0

for y in range(h):
    sum += values[y][1]

mittel_y = sum / h

print("Mittelwert_X: {0} Mittelwert_Y: {1}".format(mittel_x, mittel_y))

#Abweichungen berechnen

for y in range(h):
    abweichung[y][0] = (values[y][0] - mittel_x) * (values[y][0] - mittel_x)
    abweichung[y][1] = (values[y][1] - mittel_y) * (values[y][1] - mittel_y)
    abweichung[y][2] = (values[y][0] - mittel_x) * (values[y][1] - mittel_y)

#Varianz berewchnen
varianz_x, varianz_y, produkt = 0,0,0
for i in range(h):
    varianz_x += abweichung[i][0] / h
    varianz_y += abweichung[i][1] / h
    produkt += abweichung[i][2] / h

print("Varianz X: {0} Varianz Y: {1} Produktmittel: {2}".format(varianz_x, varianz_y, produkt))

#PQ-Formel (Determinante)
q = math.sqrt((math.pow((varianz_x - varianz_y)/2,2) + produkt *produkt))
p = (varianz_x + varianz_y) / 2

# Ereigniswert
epsilon_1 = p + q
epsilon_2 = p - q

print("P = {0}, Q = {1}".format(p,q))
print("Epsilon_1 = {0}, Epsilon_2 = {1}".format(epsilon_1, epsilon_2))

#Eigenvektoren
eigenvektor = [0,0]
eigenvektor[0] = -produkt
eigenvektor[1] = varianz_x - epsilon_1

print("Eigenvektor = ({0},{1}".format(eigenvektor[0], eigenvektor[1]))

#Was ist nochmal CP ??? Rotation
cp_vektor = [0,0]
cp_vektor[0] = eigenvektor[1] / math.sqrt(math.pow(eigenvektor[0],2)+ math.pow(eigenvektor[1],2))
cp_vektor[1] = eigenvektor[0] / math.sqrt(math.pow(eigenvektor[0],2)+ math.pow(eigenvektor[1],2))
print("CP = ({0},{1}".format(cp_vektor[0], cp_vektor[1]))

xy_verschoben = [[0 for x in range(w)] for k in range(h)]

for i in range(h):
    xy_verschoben[i][0] = values[i][0] - mittel_x
    xy_verschoben[i][1] = values[i][1] - mittel_y


xy_rotiert = [[0 for x in range(w)] for k in range(h)]
for i in range(h):
    xy_rotiert[i][0] = xy_verschoben[i][0] * cp_vektor[1] + xy_verschoben[i][1] * cp_vektor[0] + mittel_x
    xy_rotiert[i][1] = xy_verschoben[i][1] * cp_vektor[1] - xy_verschoben[i][0] * cp_vektor[0] + mittel_y

# Sortieren
xy_sorted = sorted(xy_rotiert, key=lambda x: x[0])
print(xy_sorted)

intervalle = 5

# Points per interval
points_per_interval = math.ceil(h / intervalle)

xy_intervalliesiert = [[0 for x in range(w)] for k in range(h)]

xy_tmp = [[0 for x in range(w)] for k in range(points_per_interval)]

counter = 0
interval = 0

for i in range(h):

    # Neuer Punkt zum aktuellen Intervall hinzufügen
    xy_tmp[i] = xy_sorted[i]
    counter += 1

    # Wenn das Intervall voll ist
    if(counter >= points_per_interval):
        counter = 0

        interval+=1






#plt.scatter(*zip(*xy_rotiert))
#plt.show()