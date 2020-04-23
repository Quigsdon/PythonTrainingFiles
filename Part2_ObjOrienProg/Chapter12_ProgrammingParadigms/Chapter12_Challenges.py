# Chapter 12 Challenges

import math

#1

class Apple():
    def __init__(self, w, c, t, p):
        self.weight = w
        self.color = c
        self.type = t
        self.price = p
        print("Created a apple object!")

#2

class Circle():
    def __init__(self, r):
        self.radius = r
        print("Created a cricle object!")

    def area(self):
        return self.radius * self.radius * math.pi

#3

class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("Created triangle object")

    def area(self):
        return (self.base * self.height)/2

#4

class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
        print("Created hexagon object")

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 +self.s6


    

    

    
