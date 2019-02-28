import bpy
import mathutils

print("Hello World")

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=True)

bpy.ops.mesh.primitive_cube_add()

# newly created cube will be automatically selected
cube = bpy.context.selected_objects[0]
# change name
cube.name = "FirstCube"

# change its location
cube.location = (0.0, 5.0, 0.0)
cube.keyframe_insert(data_path="location", frame=50)


cube.location = (0.0, 0.0, 0.0)
cube.keyframe_insert(data_path="location", frame=1)

cube.rotation_euler=(1, 0,0)
cube.scale=(2,1,1)

M4x4 = mathutils.Matrix([(1, 0.0000, 0.0000, 0.0000),
               (0.0000, 1, 0.0000, 0.0000),
               (0.0000, 0.0000, 1, 0.0000),
               (0.0000, 0.0000, 0.0000, 1)])
# Create a 4x4 copy:

# Assign 4x4 matrix to the object:
cube.matrix_world = M4x4
cube.keyframe_insert(data_path="rotation_euler", frame=0)
cube.keyframe_insert(data_path="location", frame=0)
cube.keyframe_insert(data_path="scale", frame=0)











