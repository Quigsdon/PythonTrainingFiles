#Chapter 13 Challenges

#1

class Shape():
    #def __init__(self, w, l):
        #self.width = w
        #self.len = l

    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len)*2

class Square(Shape):
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self, change):
        self.len += change

r1 = Rectangle(2, 4)
sq1 = Square(5)

#2
#3
#4

class Horse():
    def __init__(self, name):
        self.name = name

class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse


redrum_the_horse = Horse("Redrum")
jimmy = Rider("Jockey Jimmy", redrum_the_horse)

