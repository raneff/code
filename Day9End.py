import bpy

print(list(bpy.data.objects))

Cube = bpy.data.objects["Cube"]
print(Cube.location)

startX = 20
startY = -10
startZ = 0

endX = 0
endY = 0
endZ = 0

srX = 0
srY = 2
srZ = 1.5

erX = 0
erY = 0
erZ = 0

numFrames = 25


# Blender stores these a a matrix
# Translation
# Rotation
# Scale as matrix operations



for i in range(numFrames):
    
    endC = i/numFrames
    startC= 1 - endC
    
    Cube.location = (startC * startX + endC * endX, startC * startY + endC * endY, startC * startZ + endC * endZ)
    Cube.rotation_euler = (startC * srX + endC * erX, startC * srY + endC * erY, startC * srZ + endC * erZ)
    Cube.keyframe_insert(data_path="location", frame=i+1)
    Cube.keyframe_insert(data_path="rotation_euler", frame=i+1)








#Cube.keyframe_insert(data_path="scale", frame=1)

#Cube.location = (1,1,1)
#Cube.rotation_euler = (0,1,0)
#Cube.scale = (1,2,5)

#Cube.keyframe_insert(data_path="location", frame=10)
#Cube.keyframe_insert(data_path="rotation_euler", frame=10)
#Cube.keyframe_insert(data_path="scale", frame=10)

