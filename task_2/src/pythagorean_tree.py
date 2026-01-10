import math
import turtle


class PythagoreanTree:
    def __init__(self, width=1200, height=800):
        self.screen = turtle.Screen()
        self.screen.setup(width=width, height=height)
        self.screen.title("Дерево Піфагора")
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(0, -250)

    def draw_tree(self, length, depth):
        if depth == 0:
            return

        self.turtle.pendown()
        self.turtle.forward(length)
        self.turtle.penup()

        length_calculated = length * math.cos(math.radians(45))

        if depth - 1 == 0:
            return

        self.turtle.left(45)
        self.draw_tree(length_calculated, depth - 1)
        self.turtle.backward(length_calculated)

        self.turtle.right(90)
        self.draw_tree(length_calculated, depth - 1)
        self.turtle.backward(length_calculated)
        self.turtle.left(45)

    def visualize(self, depth):
        initial_length = 150
        self.turtle.left(90)

        self.draw_tree(initial_length, depth)

        self.screen.mainloop()
        self.turtle.done()
