# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = 1400, 800
def wall(left_bottom_x, left_bottom_y, right_top_x, right_top_y, step_x, step_y):
    left_bottom_x, left_bottom_y,  = 0, 0
    right_top_x, right_top_y = 0, 0
    step_x, step_y = 100, 50
    for i in range(8):
        left_bottom_y = i * step_y
        right_top_y = i * step_y + step_y
        if i % 2 == 0:
            for j in range(7):
                left_bottom_x = j * step_x - step_x / 2
                right_top_x = j * step_x + step_x / 2
                sd.rectangle(left_bottom=sd.get_point(left_bottom_x, left_bottom_y),
                     right_top=sd.get_point(right_top_x, right_top_y), color=sd.COLOR_ORANGE, width=0)
                sd.rectangle(left_bottom=sd.get_point(left_bottom_x, left_bottom_y),
                         right_top=sd.get_point(right_top_x, right_top_y), color=sd.COLOR_BLACK, width=3)
        else:
            for r in range(7):
                left_bottom_x = r * step_x
                right_top_x = step_x + r * step_x
                sd.rectangle(left_bottom=sd.get_point(left_bottom_x, left_bottom_y),
                     right_top=sd.get_point(right_top_x, right_top_y), color=sd.COLOR_ORANGE, width=0)
                sd.rectangle(left_bottom=sd.get_point(left_bottom_x, left_bottom_y),
                         right_top=sd.get_point(right_top_x, right_top_y), color=sd.COLOR_BLACK, width=3)

wall(left_bottom_x=0, left_bottom_y=0, right_top_x=0, right_top_y=0, step_x=100, step_y=50)
sd.pause()