# import turtle
#
# def rectangle(width, height):
#     for _ in range(2):
#         turtle.forward(width)
#         turtle.right(90)
#         turtle.forward(height)
#         turtle.right(90)
#
# w = int(input('Введите ширину: '))
# h = int(input('Введите высоту: '))

# import turtle
#
# def trianle(side):
#   turtle.right(60)
#   turtle.forward(side)
#   for _ in range(2):
#       turtle.right(120)
#       turtle.forward(side)
#
# trianle(input('Сторона = '))

# a=int(input())
# print(*[f'Объём = {a**3}', f'Площадь полной поверхности = {6*a**2}'], sep='\n')

import turtle as t

def square(side):
  t.setheading(180)
  for _ in range(3):
    t.right(22)
    for _ in range(4):
      t.forward(side)
      t.right(90)

square(int(input()))

import turtle as t

def square(side):
  for _ in range(2):
    t.right(45)
    for _ in range(4):
      t.right(90)
      for _ in range(4):
        t.forward(side)
        t.right(90)

square(int(input()))

import turtle as t

def hexagon(side):
  for _ in range(6):
    t.forward(side)
    t.right(60)

hexagon(int(input()))

#Рисует соты
import turtle as t

def hexagon(side):
  for _ in range(6):
    t.forward(side)
    t.right(60)

a = int(input())

for _ in range(6):
   hexagon(a)
   t.forward(a)
   t.left(60)

#Снежинка из 10 ромбов:
import turtle as t
for _ in range(10):
  t.right(36)
  import turtle as t
  for _ in range(2):
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)
