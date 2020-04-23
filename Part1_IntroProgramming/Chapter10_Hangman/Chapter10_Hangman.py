import random

wordList = ["cat",
            "mouse",
            "dog",
            "rat",
            "bear",
            "squirrel",
            "bird",
            "lion",
            "tiger",
            "giraffe",
            "elephant",
            "badger"
            ]

            
 

def Hangman():
    word = wordList[random.randrange(0, len(wordList)+1)]
    wrong = 0
    stages = ["",
              "______      ",
              "|           ",
              "|     |     ",
              "|     0     ",
              "|    /|\    ",
              "|    / \    ",
              "|           ",
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print ("Welcome to Hangman")

    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print("  ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))
        
    
    
