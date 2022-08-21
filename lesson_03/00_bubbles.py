# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1450, 600)

# point = sd.get_point(100, 100)
# sd.circle(center_position=point)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# point = sd.get_point(600, 250)
# radius = 50
# for _ in range (3):
# radius += 5
# sd.circle(center_position=point, radius=radius, width = 2)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
RandomColor = sd.random_color()


def bubble(point, step):
    radius = 40
    RandomColor = sd.random_color()
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=RandomColor)


# point = sd.get_point(600, 300)
# bubble(point=point, step=10)
# Нарисовать 10 пузырьков в ряд
# for x in range(100, 1450, 140):
# point = sd.get_point(x, 100)
# bubble(point=point, step=5)
# Нарисовать три ряда по 10 пузырьков
# for y in range (100, 391, 130):
# for x in range(100,1450,10):
# point = sd.get_point(x, y)
# bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(5, 10)

    bubble(point=point, step=step)

sd.pause()
