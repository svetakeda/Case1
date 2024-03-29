# Case-study #1
# Developers:
#
#
import turtle
import math
import time

def paragram1(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(math.sqrt(2)*a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(math.sqrt(2)*a)
    turtle.right(135)
    turtle.end_fill()
    pass

def paragram2(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.begin_fill()
    turtle.down()
    turtle.right(45)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    pass

def paragram3(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.forward(a)
    turtle.begin_fill()
    turtle.down()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(45)
    turtle.end_fill()
    pass

def paragram4(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.forward(a)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(45)
    turtle.end_fill()
    pass

def square1(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    pass

def square2(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.forward(a/math.sqrt(2))
    turtle.down()
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.end_fill()
    pass

def triangle1(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.right(90)
    turtle.forward(a)
    turtle.down()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(math.sqrt(2)*a)
    turtle.right(135)
    turtle.end_fill()
    pass

def triangle2(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(135)
    turtle.end_fill()
    pass

def triangle3(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.down()
    turtle.begin_fill()
    turtle.setposition(x, y)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(135)
    turtle.end_fill()
    pass

def triangle4(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.down()
    turtle.begin_fill()
    turtle.setposition(x, y)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    pass

def triangleleft(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.forward(a/2)
    turtle.down()
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(0.5)*a)
    turtle.right(90)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(45)
    turtle.end_fill()
    pass

def triangleright(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.down()
    turtle.setposition(x, y)
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(math.sqrt(0.5)*a)
    turtle.right(90)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    pass

def triangleup(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.setposition(x, y)
    turtle.up()
    turtle.forward(a/2)
    turtle.down()
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(45)
    turtle.end_fill()
    pass

def triangledown(x,y,a,color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.setposition(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(90)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(135)
    turtle.end_fill()
    pass

#TODO:(Kirill) Functions drawing pictures 1,2,3
#TODO:(Sveta) Functions drawing pictures 4,5,6
#TODO:(Vova) Functions drawing pictures 7,8,9

def main():
    '''
    Main function.
    :return: None
    '''
#paragram4(0,0,100,'blue')
triangledown(0,0,100,"green")
