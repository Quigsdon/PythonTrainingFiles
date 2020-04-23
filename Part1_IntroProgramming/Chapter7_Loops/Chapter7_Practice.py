name = "Ted"

for i in name:
    print(i)

shows = ["GOT",
         "Narcos",
         "Vice"]

coms = ("A. Development",
        "Friends",
        "Always Sunny")

people = {"G. Bluth": "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny"
          }

tv = ["GOT",
      "Narcos",
      "Vice"]
i = 0

for show in tv:
    #new = tv[i]
    #new = new.capitalize()
    tv[i] = tv[i].upper()
    i += 1

print(tv)

for i, show in enumerate(tv):
    tv[i] = tv[i].capitalize()

print(tv)

all_shows = []

for i in tv:
    i = i.upper()
    all_shows.append(i)

for i in coms:
    i = i.upper()
    all_shows.append(i)

print(all_shows)

x=10

while x>0:
	print("{}".format(x))
	x -= 1

print("Happy New Year!")

qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]
n=0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1)%3

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1

while i <=5:
    if i == 3:
        i += 1
        continue
    print(i)
    i +=1

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

added = []

for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

while input("y or n?") != "n":
    for i in range(0, 6):
        print(i)




