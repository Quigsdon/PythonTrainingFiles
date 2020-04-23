rock = []
country = []

def collect_songs():
    song = "Enter a song."
    ask = "Type r or c. q to quit"

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre == "c":
            cy = input(song)
            country.append(cy)

        else:
            print("Invalid")

    print(rock)
    print(country)

class Orange():
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

or1 = Orange(4, "light orange")
or2 = Orange(8, "dark orange")
or3 = Orange(12, "yellow")

or4 = Orange(6, "orange")
print(or4.mold)
or4.rot(10, 98)
print(or4.mold)

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())

