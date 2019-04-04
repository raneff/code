import png
import math

print("Starting our ray tracer")

# Set a pixel to a certain color at a certain point
# This requires a little math since we keep colors in a 1D array
# with three entries, [R,G,B] for each pixel
def setColor(x,y,color):
  buffer[y*(width*3)+x*3] = clamp(color[0])
  buffer[y*(width*3)+x*3 + 1] = clamp(color[1])
  buffer[y*(width*3)+x*3 + 2] = clamp(color[2])

def clamp(number):
  return max(0, min(255, abs(math.ceil(number))))

def lengthSquared(l):
  return sum([x**2 for x in l])

def length(l):
  return math.sqrt(lengthSquared(l))

def normalized(l):
  return [x/length(l) for x in l]

def dot(a, b):
  return sum([x*y for x,y in zip(a,b)])

def add(a,b):
  return [x+y for x,y in zip(a,b)]

def sub(a,b):
  return [x-y for x,y in zip(a,b)]

def mult(l, a):
  return [x*a for x in l]

# Setup our output image
width = 256
height = 256

buffer = [128 for x in range(width*height * 3)]   #Where we store our pixel data


#Setup our camera
cameraLoc = [0,0,0]                 #Where the camera is looking from
cameraLookAt = [0,0,-1]             #Where the camera is looking at
cameraHalfAngle = math.pi/2         #The half width of the field of view
extent = math.sin(cameraHalfAngle)  # Given our field of view, what is the half height of our field of view at our look at point?
doubleExtent = extent * 2           #Given our field of view, what is the full height at our look at point?

backgroundColor = [0, 0, 0]       #The background color, or the color we use if our ray doesn't hit anything

lightDirection = [0,1,0]            #The direction to an infinitely distant light source (e.g. sun)
lightDirection = normalized(lightDirection)

ambient = [25,25,25]

#Information about our circle
center = [0, 0, -1]                 #The center of the circle
r = .5                              #The radius of the circle
circleColor = [255,255,0]               #The diffuse color of the circle

#Go through and do the ray tracing

for y in range(height):             #Loop over the rows
  for x in range(width):            #Loop over the columns
    #Calculate the un-normalize direction of our ray
    targetZ = cameraLookAt[2]       #Clearly, we are pointing at the look at Z coordinate
    
    #interpolate to figure out where we are looking in x and y
    

    #convert to world coordinates
   
    #Flip so positive y is up

    setColor(x,y,backgroundColor)



#Write the buffer out to a file
f = open('swatch.png', 'wb')
w = png.Writer(width, height)
w.write_array(f, buffer)
f.close()
