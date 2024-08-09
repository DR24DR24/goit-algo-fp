import turtle
import math



def pythagoras_tree(t:turtle.Turtle, branches:list):
    tree_angl=math.pi/4*1.1
    while branches:
        pos,angl,size,order=branches.pop()
        t.penup()
        t.goto(pos)
        t.pendown()
        t.seth(180*angl/math.pi)
        t.forward(size)
        if order>=0:
            branches.append([t.pos(),angl-(math.pi/2-tree_angl),size*math.sin(tree_angl),order-1])
            branches.append([t.pos(),angl+tree_angl,size*math.cos(tree_angl),order-1])
  

def draw_pythagoras_tree(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    # t.penup()
    # t.goto(0,-size )
    # t.pendown()

    
    branches=[[(0,-size*1.5),math.pi/2,size,order]]
    

    pythagoras_tree(t,branches)

    window.mainloop()

# Виклик функції
print("windblown Pythagoras tree")
order=int(input("Input recursion order: "))
draw_pythagoras_tree(order)


