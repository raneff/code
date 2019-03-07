import bpy
import mathutils
import math
from math import pi
from mathutils import Matrix
from mathutils import Vector

print("Hello World")

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=True)

bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.selected_objects[0]
cube.name = "FirstCube"
#Assign a color
matFirstCube = bpy.data.materials.new("PKHG")
matFirstCube.diffuse_color = (.9,1.0,.1)
cube.active_material=matFirstCube

#You can define matrices by hand
M4x4 = mathutils.Matrix([(1, 0.0000, 0.0000, 0.0000),
               (0.0000, 1, 0.0000, 0.0000),
               (0.0000, 0.0000, 1, 0.0000),
               (0.0000, 0.0000, 0.0000, 1)])
               
#Or you can do it with helper functions
               
#The effect of matrices reads righ to left!!!
m =  Matrix.Translation((0,0,5)) * Matrix.Scale(2, 4) * Matrix.Rotation(pi/4, 4, 'X');

# Assign 4x4 matrix to the object:
cube.matrix_world = m
cube.keyframe_insert(data_path="rotation_euler", frame=1)
cube.keyframe_insert(data_path="location", frame=1)
cube.keyframe_insert(data_path="scale", frame=1)

##Notice the difference if we rearrange the order of operations

#bpy.ops.mesh.primitive_cube_add()
#secondCube= bpy.context.selected_objects[0]
#secondCube.name = "secondCube"
##Assign a color
#matSecondCube = bpy.data.materials.new("PKHG")
#matSecondCube.diffuse_color = (.9,0,.1)
#secondCube.active_material=matSecondCube


#               
##Notice the change in the translation's position!!!
#secondMatrix =  Matrix.Scale(2, 4) * Matrix.Rotation(pi/4, 4, 'X') * Matrix.Translation((0,0,5)) ;

## Assign 4x4 matrix to the object:
#secondCube.matrix_world = secondMatrix
#secondCube.keyframe_insert(data_path="rotation_euler", frame=1)
#secondCube.keyframe_insert(data_path="location", frame=1)
#secondCube.keyframe_insert(data_path="scale", frame=1)
