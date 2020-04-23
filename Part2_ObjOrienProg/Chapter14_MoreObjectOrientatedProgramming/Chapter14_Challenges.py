#Chapter 14 Challenges:

#1, 2

class Square():

    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append((self.len))

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)

sq1 = Square(5)
sq2 = Square(6)

print(Square.square_list)

#3

def compare(a, b):
    return a is b
        

    
