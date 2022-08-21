# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
sd.resolution = (1000, 600)
sd.background_color=sd.COLOR_GREEN
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_x = 50
start_y = 50
end_x = 350
end_y = 450
step_x = 5
step_y = 5

#for i in range(len(rainbow_colors)):
   # start_x += i * step_x
    #start_y += i * step_y
    #end_x += i * step_x
    #end_y += i * step_y
    #sd.line(start_point=sd.get_point(start_x, start_y), end_point=sd.get_point(end_x, end_y), color=rainbow_colors[i],
            #width=4)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(500, -150)


def rainbow (point, step):
    radius = 300
    for i in range(len(rainbow_colors)):
        radius += step
        sd.circle(center_position=point, radius=radius, width=25, color=rainbow_colors[i])
rainbow(point= point, step=25)
sd.pause()

