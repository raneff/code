print("start")

f = open("tri.obj", "w")

vertices = []
faces = []

vertices.append("v 0 0 0")
vertices.append("v 1 0 0")
vertices.append("v 0 1 0")

faces.append("f 1 2 3")

string = "\n".join(vertices) + "\n" + "\n".join(faces)

f.write(string)

print("end")
