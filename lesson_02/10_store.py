#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп


# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб


lamps_quantity = store[goods['Лампа']][0]['quantity']
lamps_cost = lamps_quantity * store[goods['Лампа']][0]['price']

print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')





tables_quantity_1= store[goods['Стол']][0]['quantity']
tables_cost_1 = tables_quantity_1 * store[goods['Стол']][0]['price']
tables_quantity_2= store[goods['Стол']][1]['quantity']
tables_cost_2 = tables_quantity_2 * store[goods['Стол']][1]['price']

tables_quantity = tables_quantity_1 + tables_quantity_2
tables_cost = tables_cost_1 + tables_cost_2

print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')




chairs_quantity_1 = store[goods['Стул']][0]['quantity']
chairs_cost_1 = chairs_quantity_1 * store[goods['Стул']][0]['price']
chairs_quantity_2 = store[goods['Стул']][1]['quantity']
chairs_cost_2 = chairs_quantity_2 * store[goods['Стул']][1]['price']
chairs_quantity_3 = store[goods['Стул']][2]['quantity']
chairs_cost_3 = chairs_quantity_3 * store[goods['Стул']][2]['price']

chairs_quantity = chairs_quantity_1 + chairs_quantity_2 + chairs_quantity_3
chairs_cost = chairs_cost_1 + chairs_cost_2 + chairs_cost_3

print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')



sofas_quantity_1 = store[goods['Диван']][0]['quantity']
sofas_cost_1 = sofas_quantity_1 * store[goods['Диван']][0]['price']
sofas_quantity_2 = store[goods['Диван']][1]['quantity']
sofas_cost_2 = sofas_quantity_2 * store[goods['Диван']][1]['price']

sofas_quantity = sofas_quantity_1 + sofas_quantity_2
sofas_cost = sofas_cost_1 + sofas_cost_2

print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






