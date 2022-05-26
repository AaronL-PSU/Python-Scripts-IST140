import turtle
while True:
    t = turtle.Turtle()
    locx = int(input("Enter shape's x location: "))
    locy = int(input("Enter shape's y location: "))
    shape = input("Would you to draw a circle or a rectangle?: ")

    if shape == "circle":
        t.shapesize(1,1,1)
        t.shape("circle")
        rad = int(input("Enter the radius of the circle: "))
        t.penup()
        t.goto(locx, locy)
        t.pendown()
        t.circle(rad)
    elif shape == "rectangle":
        t.shapesize(1,1,1)
        t.shape("square")
        width = int(input("Enter the width: "))
        height = int(input("Enter the height: "))
        t.penup()
        t.goto(locx, locy)
        t.pendown()
        t.goto(locx+width, locy)
        t.goto(locx+width, locy+height)
        t.goto(locx, locy+height)
        t.goto(locx, locy)
    else:
        print("Enter the name of a shape")

    stop = input("Do you want to continue? y/n")
    if stop == "n" or "N" or "No" or "no":
        break
