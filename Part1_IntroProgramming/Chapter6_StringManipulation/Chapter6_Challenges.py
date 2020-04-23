#Chapter 6 Challenges

#1

q1 = "Camus"

print(q1)

print(q1[0:])



for i in range(0, len(q1)):
    print(q1[i])
    i +=1

#2

q2a = input("Enter a noun:")
q2b = input("Enter a person:")

q2r = "Yesterday I wrote a {}. I sent it to {}!".format(q2a,
                                                        q2b)

print(q2r)

#3

q3a = "aldous Huxley was born in 1894."

print(q3a.capitalize())

#4

q4a = "Where now? Who now? When now?"
print(q4a.split("?"))

#5

words = ["The",
         "fox",
         "jumped",
         "over",
         "the",
         "fence",
         "."]

q5a = " ".join(words)
q5a = q5a.replace(" .",".")
print(q5a)

#6

q6a = "A screaming comes across the sky."
print(q6a.replace("s","$"))

#7

q7a = "Hemingway"
print(q7a.index("m"))

#8

q8a = "'Let there be rock', to which i stated 'yes!'"
print(q8a)

#9

q9a = "three"

print(q9a * 3)
print(q9a + " " + q9a + " " + q9a)

#10

q10a = "It was a bright cold day in April, and the clocks were striking thirteen."
q10a.index(",")
print(q10a[:q10a.index(",")])


