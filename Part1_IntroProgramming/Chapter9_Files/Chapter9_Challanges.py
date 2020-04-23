#Chapter 9 Challenges:

import os
import csv

#1

filePath1 = os.path.join("C:/",
                        "Users",
                        "mqsil",
                        "Desktop",
                        "Coding",
                        "st.txt")

with open(filePath1, "r") as f:
    print(f.read())

#2

q2 = input("What is your favourite colour?")

filePath2 = os.path.join("C:/",
                         "Users",
                         "mqsil",
                         "Desktop",
                         "Coding",
                         "TheSelfTaughtProgrammer",
                         "Part1",
                         "Chapter9_Files",
                         "q2Challenge.txt")

with open(filePath2, "w") as f:
    f.write(q2)




#3

filePath3 = os.path.join("C:/",
                         "Users",
                         "mqsil",
                         "Desktop",
                         "Coding",
                         "TheSelfTaughtProgrammer",
                         "Part1",
                         "Chapter9_Files",
                         "q3Challenge.csv")

q3 = [["Top Gun",
        "Risky Business",
        "Minority Report"],
       ["Titanic",
        "The Revenant",
        "Inception"],
       ["Training Day",
        "Man on Fire",
        "Flight"]
       ]


with open(filePath3, "w", newline="") as f:
    w = csv.writer(f,
                   delimiter=",")
    for i in range(0, len(q3)):
        w.writerow(q3[i])
