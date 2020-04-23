# Chapter 4 Challenges

#1

def sq(x):
    return x **2

#2


def pStr(x):
    print(x)


#3

def fiveInputs(a,b,c,d=10,e=20):
    return a+b+c+d+e

#4

def div2(x):
    return x/2

def mult4(x):
    return x*4

c4q4res = div2(6)

print(mult4(c4q4res))

#5

def convStoF(x):
    """ Takes value of x, trys to convert to string. prints
    value as string if possible, otherwise prints error
    message.
    :param x: string
    :return: string converted to float"""
    try:
        print(float(x))
    except ValueError:
        print("Error, cannot convert to a float")

#6
        




    
