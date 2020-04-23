class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width*self.len
        
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        #clients can use this
        pass

    def _unsafe_method(self):
        #clients shouldn't use this
        pass

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
            """.format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len
    def print_size(self):
        print("""I am {} by {}
            """.format(self.width, self.len))

class Dog():
    def __init__(self,
                 name,
                 breed,
                 owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)

