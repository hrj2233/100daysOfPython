# import colorgram
import turtle as turtle_module
import random
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(246, 242, 234), (248, 240, 244), (236, 246, 240), (239, 242, 248), (216, 148, 92), (221, 78, 57), (45, 94, 146), (151, 64, 91), (232, 219, 93), (217, 65, 85), (22, 27, 41), (40, 22, 29), (120, 167, 197), (40, 19, 14), (194, 139, 159), (159, 72, 56), (35, 132, 91), (123, 181, 142), (69, 167, 94), (236, 222, 6), (170, 176, 42), (231, 168, 182), (14, 30, 21), (51, 54, 105), (106, 42, 61), (25, 168, 202), (236, 171, 161), (107, 44, 37), (163, 210, 185), (150, 207, 222)]

tim.setheading(235)
tim.forward(300)
tim.setheading(0)
number_of_dots =100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()