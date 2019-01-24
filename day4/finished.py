# Code for generating an OBJ file that represents a sphere
# Written by B. Ricks for U_n@Omaha CSCI 4620, Computer Graphics, Spring 2019
# Note that this code does not correctly wind triangles (i.e. half are wound clockwise and half are counter clockwise)
# This is intentional since in a 3D editor (e.g. Blender) students can see the actual triangles
# In production, flip a vertex on one of the triangles for consistency.

import math

print("start")

f = open("tri.obj", "w")

vertices = []
faces = []

# Radius of circle
radius = 1
# The library we use decides radians or degrees for us.

#Number of lines that go around the circle (think longitude lines)
lines = 12

#Number of rings (think latitude lines/2)
rings = 5

currentDegrees = 0 #Tracks how far around the equator we have gone
currentVertex = 1 #Tracks which vertex we are at. A simple counter for keeping faces and vertices in sync

for i in range(lines):
    currentRadius = radius
    currentHeight = 0
    for j in range(rings):

      #We need to know where the next latitude line is for creating the triangles
        nextAngle = 3.141/2 / rings * (j + 1)
        nextRadius = math.cos(nextAngle) * radius
        nextHeight = math.sin(nextAngle) * radius

        # Calculate the values for the current radius

        x = math.cos(currentDegrees) * currentRadius
        y = math.sin(currentDegrees) * currentRadius
        x2 = math.cos(currentDegrees + 2*3.14/lines) * currentRadius
        y2 = math.sin(currentDegrees + 2 * 3.14/lines) * currentRadius

        radius2 = nextRadius

        # Calculate the values for the the next radius up

        xs = math.cos(currentDegrees) * radius2
        ys = math.sin(currentDegrees) * radius2
        x2s = math.cos(currentDegrees + 2*3.14/lines) * radius2
        y2s = math.sin(currentDegrees + 2 * 3.14/lines) * radius2

        #Use these values to create two pairs of triangle (one pair for the top hemispher and one set for the bottom hemisphere)
        
        vertices.append("v " + str(x) + " " + str(y) + " " + str(currentHeight))
        vertices.append("v " + str(x2) + " " + str(y2) + " " + str(currentHeight))          
        vertices.append("v " + str(xs) + " " + str(ys) + " " + str(nextHeight))
        
        vertices.append("v " + str(xs) + " " + str(ys) + " " + str(nextHeight))
        vertices.append("v " + str(x2s) + " " + str(y2s) + " " + str(nextHeight))
        vertices.append("v " + str(x2) + " " + str(y2) + " " + str(currentHeight))

        vertices.append("v " + str(x) + " " + str(y) + " " + str(-currentHeight))
        vertices.append("v " + str(x2) + " " + str(y2) + " " + str(-currentHeight))          
        vertices.append("v " + str(xs) + " " + str(ys) + " " + str(-nextHeight))
        
        vertices.append("v " + str(xs) + " " + str(ys) + " " + str(-nextHeight))
        vertices.append("v " + str(x2s) + " " + str(y2s) + " " + str(-nextHeight))
        vertices.append("v " + str(x2) + " " + str(y2) + " " + str(-currentHeight))

        # Append the face information for the two pairs of triangles


        faces.append("f " + str(currentVertex + 0) + " " + str(currentVertex + 1) + " " + str(currentVertex + 2))
        faces.append("f " + str(currentVertex + 3) + " " + str(currentVertex + 4) + " " + str(currentVertex + 5))

        faces.append("f " + str(currentVertex + 6) + " " + str(currentVertex + 7) + " " + str(currentVertex + 8))
        faces.append("f " + str(currentVertex + 9) + " " + str(currentVertex + 10) + " " + str(currentVertex + 11))

        
        currentRadius = radius2
        currentHeight = nextHeight

        currentVertex = currentVertex + 12
    currentDegrees = currentDegrees + 2*3.14/lines

string = "\n".join(vertices) + "\n" + "\n".join(faces)

f.write(string)

print("end")
