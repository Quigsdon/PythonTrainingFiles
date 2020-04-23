# Chapter 7 challenges

#1

q1a = ["The Walking Dead",
       "Entourage",
       "The Sopranos",
       "The Vampire Diaries"]

for i in q1a:
    print(i)

#2

x= 25

while x <=50:
    print(x)
    x+=1

#or:

for i in range(25, 51):
    print(i)

#3


for i in range(0, len(q1a)):
    print(q1a[i])
    print(i)

#or

for i, show in enumerate(q1a):
    print(i)
    print(show)

#4

list4 = [1, 5, 6, 8, 9]

while input("type q to quit or any other button to continue") != "q":
    a = input("guess a number between 1 and 10")
    try:
        a = int(a)
    except ValueError:
        print("please type a number or q to quit")
    
    if a in list4:
        print("you guessed correctly!")
    else:
        print("you guessed incorrectly, please try again")

#or

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit")
    if answer in list4:
        print ("You guessed correctly!")
    else:
        print("you guessed incorrectly!")
    

#5

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

multiplied = []

for i in list1:
    for j in list2:
        multiplied.append(i*j)

print(multiplied)
