# import colorgram
import random
import turtle as t

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


tim = t.Turtle()
t.colormode(255)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
              (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
x_cor = -200.0
y_cor = -200.0
dot_count = 10
row_count = 10
tim.speed(9)

for x in range(row_count):
    for y in range(dot_count):
        tim.penup()
        tim.goto(x_cor, y_cor)
        tim.dot(20, random.choice(color_list))
        x_cor += 50.0
    x_cor = -200.0
    y_cor += 50.0

tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
