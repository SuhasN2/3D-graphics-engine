import turtle
import numpy

# dif window ----------------------------------------------------------------------
win = turtle.Screen()
win.title("test")
win.bgcolor("black")
win.setup(width=800, height=500)

# def pen
pen = turtle.Turtle()
pen.hideturtle()
pen.shape("circle")
pen.color("white", "blue")
pen.speed(0)
pen.penup()

# functions ------------------------------------------------------------------------


# inputs ---------------------------------------------------------------------------

# Function to change the pen size
def pen_size():
    return win.numinput("pen size", "Enter pen size (1-10):",
                         default=2, minval=1, maxval=10)

# Function to change the rotate_x
def input_rotate(rotate):
    return win.numinput("rotate_"+rotate, "Enter pen size (0-360):",
                         default=45, minval=0, maxval=360)


# Function to change the focal length
def focal_length():
    FL = win.numinput("focal length", "Enter focal length (150-):",
                       default=450, minval=150, maxval=1500)
    return FL

# Function to change the angle
def angleF():
    angle = win.numinput("angle", "Enter angle (1-150):",
                       default=150, minval=0, maxval=500)
    return angle

# 3D object ------------------------------------------------------------------------

Vertex_3D = [
    [0, 0, 0],
    [-50, 50, 250],
    [50, 50, 250],
    [50, -50, 250],
    [-50, -50, 250],

    [-50, 50, 200],
    [50, 50, 200],
    [50, -50, 200],
    [-50, -50, 200],
]

Edge_3D = [
     [1,2],
     [2,3],
     [3,4],
     [4,1],

     [5,6],
     [6,7],
     [7,8],
     [8,5],

     [1,5],
     [2,6],
     [3,7],
     [4,8],
]


# camera ---------------------------------------------------------------------------

def calculate_screen_vertex(X, Y, Z, fl):
    return (X / (Z + fl))* fl , (Y / (Z + fl))* fl 

def draw_screen_edge(x1, y1, x2, y2):
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

# Basic rotations ------------------------------------------------------------------

def rotate_x(theta):
    c = numpy.cos(theta)
    s = numpy.sin(theta)
    return numpy.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ])

def rotate_y(theta):
    c = numpy.cos(theta)
    s = numpy.sin(theta)
    return numpy.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])

def rotate_z(theta):
    c = numpy.cos(theta)
    s = numpy.sin(theta)
    return numpy.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ])

X = input_rotate("X")
Y = input_rotate("Y")
Z = input_rotate("Z")
# render ---------------------------------------------------------------------------

for k in range(1):
    Vertex_2D = []

    FL = focal_length()
    angle = angleF()
    pen.pensize(pen_size())
    
    for j in Vertex_3D:
        Vertex_2D.append(numpy.dot(rotate_x(angle),X))
        Vertex_2D.append(numpy.dot(rotate_y(angle),Y))
        Vertex_2D.append(numpy.dot(rotate_x(angle),Z))
    print(Vertex_2D)
    print("------------------------------------------------------------------------------------------------------")
    print("           x1           |            y1            ||            x2           |           y2          ")
    print("------------------------------------------------------------------------------------------------------")
    for i in Edge_3D:
        v1 = Vertex_2D[i[0]]
        v2 = Vertex_2D[i[1]]
        x1, y1 = calculate_screen_vertex(v1[0], v1[1], v1[2], FL)
        x2, y2 = calculate_screen_vertex(v2[0], v2[1], v2[2], FL)
        print(f"  {x1},   |    {y1},   ||    {x2},   |    {y2}")
        print("--------------------------------------------------------------------------------------------------")
        draw_screen_edge(x1, y1, x2, y2)
        turtle.clear()



# keep the turtle screen open until it is manually closed
# Start the event loop
print("#######################################################################################################")
turtle.mainloop()