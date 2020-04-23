rhymes = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live"
         }

n = input("Type a number:")
if n in rhymes:
    rhymes = rhymes[n]
    print(rhymes)
else:
    print("Not found.")


lists=[]
rap=["Kanye West",
     "Jay Z",
     "Eminem",
     "Nas"]

rock=["Bob Dylan",
      "The Beatles",
      "Led Zeppelin"]

djs=["Zeds Dead",
     "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print (lists)
