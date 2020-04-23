import os

# "r" open a file for reading only
# "w" opens for writing only. Overites existing or creates new
# "w+" opens for reading & writing. overwrites existing or creates new.

#st = open("st.txt", "w")
#st.write("Hi from Python!")
#st.close()

# use with-statement to automatically close file. f is just a variable.

with open("st.txt", "w") as f:
    f.write("Hi from Python using With_Statement!")

#with open("st.txt", "r") as f:
#    print(f.read())

#can only read once without closing and reopening again.
#can save as another variable:

my_list = []

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)

import csv

with open("st.csv", "w", newline="") as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])

with open("st.csv", "r") as f:
    r = csv.reader(f,
                   delimiter=",")
    for i in r:
        print(",".join(i))


