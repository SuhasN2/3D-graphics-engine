import turtle
import numpy
import time


# Create turtle screen
win = turtle.Screen()
win.title("test")
win.bgcolor("black")
win.setup(width=800, height=500)

# Create turtle pen
pen = turtle.Turtle()
pen.hideturtle()
pen.shape("circle")
pen.color("white", "blue")
pen.speed(0)
pen.penup()

# Function to print a matrix in a readable format
def print_matrix(matrix):
    print("----------------------")
    for k in matrix:
        print("| ", end = "")
        for l in k:
            print ( l, end = " ")
        print("|")
    print("----------------------")

# Functions to get user inputs
def pen_size():
    return win.numinput("pen size", "Enter pen size (1-10):", default=2, minval=1, maxval=10)

def input_rotate(rotate):
    return win.numinput("rotate_"+rotate, "Enter pen size (0-360):", default=45, minval=0, maxval=3600)

def focal_length():
    FL = win.numinput("focal length", "Enter focal length (150-):", default=450, minval=150, maxval=1500)
    return FL

# Define 3D object
camera_position = [-150, 0, 50]

Vertex_3D = [

    [0, 0, 0],

    [-50, 50, 0],
    [50, 50, 0],
    [50, -50, 0],
    [-50, -50, 0],

    [-50, 50, -50],
    [50, 50, -50],
    [50, -50, -50],
    [-50, -50, -50],

    [50, 30, 0],
    [50, 30, -50]
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

     [9,10]
]

# Define camera
camera = [0, 0, 0]

# Functions to calculate camera rotations and screen vertex coordinates
def calculate_camera_rotations(list_, matrix):
    output =[]
    for i in matrix:
        output.append( i + list_)
    return output

def rotate (Vertex,X,Y,Z):
    Vertex_2D_X = []
    Vertex_2D_X_Y = []
    Vertex_2D_X_Y_Z = []

    for x_ in Vertex:
        Vertex_2D_X.append(numpy.dot(rotate_x(X),x_))
    for y_ in Vertex_2D_X:
        Vertex_2D_X_Y.append(numpy.dot(rotate_y(Y),y_))
    for z_ in Vertex_2D_X_Y:
        Vertex_2D_X_Y_Z.append(numpy.dot(rotate_z(Z),z_))
    
    return Vertex_2D_X_Y_Z


def calculate_screen_vertex(X, Y, Z, fl):
    return (X/(Z+fl))*fl, (Y/(Z+fl))*fl 

# Function to draw screen edge
def draw_screen_edge(x1, y1, x2, y2):
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

# Basic rotation matrices
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

FL = focal_length()
pen.pensize(pen_size())

# render ---------------------------------------------------------------------------

win.tracer(0)

for frame in range(160):

    # The code calculates the 2D projection of a 3D object onto a camera's view plane by applying camera
    #  rotaprelodetions to both the camera and the object, and then using the resulting transformation to calculate
    #  the 2D coordinates of a vertex. The final 2D coordinates are assigned to the variable Vertex_2D
    
    Vertex_2D = calculate_camera_rotations(camera_position, calculate_camera_rotations(camera,rotate(Vertex_3D,X + (frame/128),Y,Z)))

    print(Vertex_2D)

    print_matrix(Vertex_2D)
    print()  
    print("-------------------------------------------------------------------------------------------------------------")
    print("           x1           |            y1            ||            x2           |           y2          ")
    print("-------------------------------------------------------------------------------------------------------------")

    preload_data_1 = []
    preload_data_2 = []

    for i in Edge_3D:
        v1 = Vertex_2D [i[0]]
        v2 = Vertex_2D [i[1]]
        x1, y1 = calculate_screen_vertex(v1[0], v1[1], v1[2], FL)
        x2, y2 = calculate_screen_vertex(v2[0], v2[1], v2[2], FL)
        list1 = [x1, y1]
        list2 = [x2, y2]
        preload_data_1.append(list1)
        preload_data_2.append(list2)
        list1 = []
        list2 = []
        # print (f"  {x1},   |    {y1},   ||    {x2},   |    {y2}   |")
        # print ("-------------------------------------------------------------------------------------------------------------")
        

    pen.reset()

    pen.hideturtle()
    pen.shape("circle")
    pen.color("white", "blue")
    pen.speed(0)
    pen.penup()

    for oj in range(len(Edge_3D)):
        draw_screen_edge (preload_data_1[oj][0] + (frame * 2), preload_data_1[oj][1]+ (2),preload_data_2[oj][0] + (frame * 2), preload_data_2[oj][1] + (2))
    win.update()
    



# keep the turtle screen open until it is manually closed
# Start the event loop
print("#######################################################################################################")
turtle.mainloop()
