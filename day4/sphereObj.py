import math

print("start")

f = open("tri.obj", "w")

vertices = []
faces = []

# Radius of circle
radius = 1
# The library we use decides radians or degrees for us.
#Number of lines in circle
lines = 12
rings = 2
currentDegrees = 0
for i in range(lines):
    currentRadius = radius
    for j in range(rings):
        x = math.cos(currentDegrees) * currentRadius
        y = math.sin(currentDegrees) * currentRadius
        x2 = math.cos(currentDegrees + 2*3.14/lines) * currentRadius
        y2 = math.sin(currentDegrees + 2 * 3.14/lines) * currentRadius

        radius2 = currentRadius * .75

        xs = math.cos(currentDegrees) * radius2
        ys = math.sin(currentDegrees) * radius2
        x2s = math.cos(currentDegrees + 2*3.14/lines) * radius2
        y2s = math.sin(currentDegrees + 2 * 3.14/lines) * radius2
        
        currentDegrees = currentDegrees + 2*3.14/lines
        vertices.append("v " + str(x) + " " + str(y) + " 0")
        vertices.append("v " + str(x2) + " " + str(y2) + " 0")          
        vertices.append("v " + str(xs) + " " + str(ys) + " 1")
        
        vertices.append("v " + str(xs) + " " + str(ys) + " 1")
        vertices.append("v " + str(x2s) + " " + str(y2s) + " 1")
        vertices.append("v " + str(x2) + " " + str(y2) + " 0")

        currentRadius = radius2



        faces.append("f " + str(i * 6 * rings + 1) + " " + str(i * 6 * rings + 2) + " " + str(i * 6 * rings + 3))
        faces.append("f " + str(i * 6 * rings + 4) + " " + str(i * 6 * rings + 5) + " " + str(i * 6 * rings + 6))

string = "\n".join(vertices) + "\n" + "\n".join(faces)

f.write(string)

print("end")
