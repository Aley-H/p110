import random
print(dir(random))

response = input("do u  want to roll")

response = "y"

while response=="y":

no=random.randint(1, 6)

if no==1:
    print("[-----]")
    print("[     ]")
    print("[  0  ]")
    print("[     ]")
    print("[-----]")

finished = input("press y to play again, press n to close: ")


















