import sys

path1 = sys.argv[1]
path2 = sys.argv[2]
coordinatesCircle = open(path1, "r")
coordinates = open(path2, "r")

def checkInCircle(coord, radius, coordDot):
    coord1 = coord.split(" ")
    coordDot2 = coordDot.split(" ")
    if (float((float(coordDot2[0]) - float(coord1[0])))**2+float((float(coordDot2[1]) - float(coord1[1])))**2 < float(radius[0])**2):
        return 1
    elif (float((float(coordDot2[0]) - float(coord1[0])))**2+float((float(coordDot2[1]) - float(coord1[1])))**2 == float(radius[0])**2):
        return 0
    return 2

answer = []
coord = coordinatesCircle.readlines()
for i in range(0, len(coord)):
    coord[i] = coord[i].rstrip()
coordDot = coordinates.readlines()
for i in range(0, len(coordDot)):
    coordDot[i] = coordDot[i].rstrip()
for i in range(0, len(coord), 2):
    radius = coord[i + 1]
    for j in range(0, len(coordDot)):
        answer.append(checkInCircle(coord[i], radius, coordDot[j]))
for result in answer:
    print(result)
