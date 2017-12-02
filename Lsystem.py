"""
L-Systems
For anybody who knows a mixture of biology, geometry, art, and programming, L-systems are for you!
L-systems take an initial axiom in the form of a single character string, and by use of some conditionals and iterative functions, 
can make more complex larger strings building off of the initial axiom (I'm sorry for the explanation, it even confuses me sometimes)
Anyway, I use the turtle module in order to visually display how the system works and looks in terms of geometric shapes
  If you reuse the code, test out different numbers, and see how the shape turns out
"""

import turtle

def applyRules(char):
    return_str = ""
    if(char == "X"):
        return_str = "X+Y[BF"
    elif(char == "Y"):
        return_str = "F]X-[BY]"
    else:
        return_str = char
    return return_str

def process(old_string):
    new_str = ''
    for c in old_string:
        new_str += applyRules(c)
    return new_str

def createLSystem(iterations, axiom):
    start_string = axiom
    end_string = ""
    for i in range(iterations):
        end_string = process(start_string)
        start_string = end_string
    return end_string

def drawLSystem(string, dist, deg):
    mert = turtle.Turtle()
    mert.speed(0)
    window = turtle.Screen()
    positions = []

    for instruction in string:
        if (instruction == 'F'):
            mert.forward(dist)
        elif (instruction == '-'):
            mert.right(deg)
        elif (instruction == '+'):
            mert.left(deg)
        elif (instruction == "["):
            head = mert.heading()
            x = mert.xcor()
            y = mert.ycor()
            state = [x, y, head]
            positions.append(state)
        elif (instruction == "B"):
            mert.left(180)
            mert.forward(dist)
        elif (instruction == "]"):
            if len(positions) != 0:
                pos = positions.pop(0)
                mert.setheading(pos[2])
                mert.goto(pos[0], pos[1])

    window.exitonclick()

def main():
    iteration = int(input("Number of iterations: "))
    final_str = createLSystem(iteration, "FX")
    distance = int(input("How far forward?: "))
    degree = int(input("How much to turn?: "))
    drawLSystem(final_str, distance, degree)
main()
