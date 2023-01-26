from rectangle import Rectangle
from rectangle import Square
from rectangle import Circle

#прямоугольники
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

#Квадаты
square_1 = Square(5)
square_2 = Square(10)

#Окружности
circle_1 = Circle(30)
circle_2 = Circle(20)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure,Circle):
        print(int(figure.area_r()))
    else:
        print(int(figure.get_area()))
