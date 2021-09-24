"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Taylor Dupuy

********* HEY, READ THIS FIRST **********

For this assignment, I created generated art that would change it's coordinate positions and color every time you run the code!
In this code, there are 4 shapes, two from squares and two from circles, using for loops I tried to make each shape produce a unique shape.
To me, this work symbolizes great progress for myself, I come from a background in science, so any semblance of art seems like a win to me.
It evokes confidence and pride in my own abilities, but to others it may seem like gibberish pee pee.
I call this piece, Personal Pride, or 'PP' for short.

"""
import turtle
import math, random

turtle.colormode(255)
turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables (I have 5!)
# You must use 2 for loops (a nested for loop counts as 2!) (Got plenty of those!)
# You must use at least 1 random element (something from the random library) (Check!)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?) (I have comments below!)

# =============== ADD YOUR CODE BELOW! =================

#first I created variable names for the different turtles that I used in the code
ls= turtle.Turtle()
ss= turtle.Turtle()
lc= turtle.Turtle()
sc= turtle.Turtle()
arrow= turtle.Turtle()


#before i switched to the tracer function, i hid the turtles so the drawing seemed more flawless. though even now I still have them off for the finished design
ls.hideturtle()
ss.hideturtle()
lc.hideturtle()
sc.hideturtle()
arrow.hideturtle()

#my use of random came in here to randomly select an x and y location based on these presets, each shape is assigned a different quadrant of the panel
#I also randomized the color of the turtle based on the RGB values
x1= random.randint(0, 150), random.randint(0, 150)
x2= random.randint(0, 150), random.randint(-150, 0)
y1= random.randint(-150, 0), random.randint(0,150)
y2= random.randint(-150, 0), random.randint(-150, 0)
lr= random.randint(0, 255)
lg= random.randint(0, 255)
lb= random.randint(0, 255)
lrgb= [lr, lg, lb]

#code for the Large Square (ls) design
ls_size= 50
ls.color(lrgb)
ls.pensize(3)
ls.penup()
ls.goto(x1)
ls.pendown()
square_angle= 30
square_numint= int(360/square_angle)
for i in range(square_numint): #creates a number of large squares in a circle based on the angle between each square!
    ls.begin_fill()
    for i in range(4): #actually makes the square lol
        ls.forward(ls_size)
        ls.left(90)
    ls.end_fill()
    ls.forward(ls_size)
    ls.right(square_angle)

#code used to design the small square, note the random function for the color!
sr= random.randint(0, 255)
sg= random.randint(0, 255)
sb= random.randint(0, 255)
srgb= [sr, sg, sb]
ss_square_angle= 60
ss_size= 25
ss.color(srgb)
ss.pensize(3)
ss.penup()
ss.goto(x2)
ss.pendown()
for i in range(square_numint):
   ss.begin_fill()
   for i in range(4):
        ss.forward(ss_size)
        ss.left(90)
   ss.end_fill()
   ss.forward(ss_size)
   ss.right(ss_square_angle)

#code for the large circle!
cr= random.randint(0, 255)
cg= random.randint(0, 255)
cb= random.randint(0, 255)
crgb= [cr, cg, cb]
inner_radius= 2
lc_radius= 50
lc.color(crgb)
lc.pensize(3)
lc.penup()
lc.goto(y1)
lc.pendown()
lc.circle(lc_radius)
angle= 10
numint= int(360/angle)
for i in range(numint): #creates the fun overlapping circles, originally I had them filled, but this ended up looking cooler!
    lc.forward(inner_radius)
    lc.right(angle)
    lc.circle(lc_radius)

#code used for the small circle
r= random.randint(0, 255)
g= random.randint(0, 255)
b= random.randint(0, 255)
rgb= [r, g, b]
sc_angle= 30
sc_radius= 25
sc.color(rgb)
sc.pensize(3)
sc.penup()
sc.goto(y2)
sc.pendown()
sc.circle(sc_radius)
for i in range(numint):
    sc.forward(inner_radius)
    sc.right(sc_angle)
    sc.circle(sc_radius)

#for this section, I used pseudocode from Amy Zhang, a fellow grad student.
#I was unsure from her psuedocode, exactly how she had planned on using the arrow, so I modified it to create a hexagon shape at the top of the panel
#if I had more time and resources, I would have liked to turn the arrows to make a clock of some sorts, that hung at the top of every iteration, possibly showing a different time each iteration? 
arrow.up()
arrow.goto(0, 300)
arrows= 6
arrow.shape("arrow")
arrow.down()

for i in range(arrows):
    arrow.forward(50)
    arrow.stamp()
    arrow.right(60)


panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
turtle.done()
