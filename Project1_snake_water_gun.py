import random
you_score = 0 ; comp_score = 0
print("\t\t\tWelcome! Its a Snake, Water ,Gun Game!")
print("'s' for Snake\n'w'for Water\n'g' for Gun")
for i in range(1,6):
    computer = random.choice([1,-1,0])
    youstr = input("Enter your choice : ")
    youDict = {"s":1, "w":-1, "g":0}
    compdict = {1:"Snake", -1:"Water", 0:"Gun"}

    if youstr not in youDict:
        print("Invalid choice: please enter 's' or 'w' or'g' ")
        continue

    you = youDict[youstr]
    print(f"You choose {compdict[you]}\ncomputer choose {compdict[computer]}")

    if(you == computer):
        print("\t\tThis round is draw")
    else:
        if(computer==1 and you==0) or (computer==0 and you==-1) or (computer==-1 and you==1):
            print("\t\tYou win this round!")
            you_score += 1
        else:
            print("\t\tComputer win this round!")
            comp_score += 1

print(f"\nYour score is {you_score}\nComputer score is  {comp_score}\n")
if(you_score > comp_score):
    print("********** You win the Game! **********")
elif(you_score < comp_score):
    print("********** Computer win the Game! **********")
else:
   print("--------- The Game is a Draw ---------")
