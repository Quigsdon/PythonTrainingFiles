#Chapter 5 Challenges

#1

FavBands = ["Led Zeppelin",
            "Tool",
            "Rammstein"]

#2

Visited = [(.123, .13413),
           (.1324, 124124),
           (-1.123, 2.2134)]

#3

Me = {"height": "tall",
      "tone":"dark",
      "looks":"handsome"}

#4

n = input("Ask about height, tone or looks:")
if n in Me:
    print(Me[n])
else:
    print("I' afraid you entered an incorrect value")

#5

FavSongs = {"Tool": "Invincible",
            "Led Zeppelin":"Stairway to Heaven",
            "Stone Roses":
            "I am the Resurrection"
            }

#6

#Sets are set of unique objects unordered (equivalent to Sets in maths). They are a data type that is iterable, mutable and has no duplicate. eg:

a=set("abracadabra")
b=set("alacazam")
print("set a (abracadabra) unique letters:")
print(a)                        # unique letters in a
print("set b (alacazam) unique letters:")
print(b)                                #unique letters in b
print("letters in a but not in b (a - b):")
print(a - b)                          # letters in a but not in b
print("letters in either a or b (a | b):")
print(a | b)                            # letters in either a or b
print("letters in both a and b (a & b):")
print(a & b)                              # letters in both a and b
print("letters in a or b but not both (a ^ b):")
print(a ^ b)                            # letters in a or b but not both

