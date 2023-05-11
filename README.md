# 3D-graphics-engine
a 3D graphics engine from scratch,
3D Object Viewer
This is a Python program that allows you to view a 3D object and rotate it around different axes. The program uses the turtle module to create a 3D turtle pen and the numpy module for matrix operations.

Requirements
This program requires Python 3 and the turtle and numpy modules to be installed. You can install these modules using pip:


pip install turtle
pip install numpy
Usage
To use the program, run the 3D_viewer.py file. This will open a window with the 3D object displayed.

The following commands are available:

Up Arrow: Move the camera up
Down Arrow: Move the camera down
Left Arrow: Move the camera left
Right Arrow: Move the camera right
8: Zoom in
2: Zoom out

not yet implemented:
shading
r: Rotate the object around the X-axis
t: Rotate the object around the Y-axis
y: Rotate the object around the Z-axis
p: Change the pen size
e: Exit the program
When you press r, t, or y, you will be prompted to enter a value between 0 and 360 to rotate the object around that axis.

When you press p, you will be prompted to enter a value between 1 and 10 to change the pen size.
