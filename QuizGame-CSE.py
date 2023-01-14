print("Welcome To Our CSE Quiz")

playing = input("Do You Want To Play?\n")

if playing.lower() !="yes":
    quit()

print("Okay! Let's Play:)")
score=0
answer=input("Which one is the First Fully supported 64-bit OS?\nOptions\n(a)Windows Vista\n(b)Mac\n(c)Linux\n(d)Windows XP\nEnter Your Option:")
if answer.lower()=="c":
    print('Exactly! Keep Going....')
    score+=1
else:
    print("Actually,I don't Think....")
answer=input("Which of the following is not a web browser?\nOptions\n(a)MOSAIC\n(b)WWW\n(c)Facebook\n(d)Netscape Navigator\nEnter Your Option:")
if answer.lower()=="c":
    print('Absolutely!!!!')
    score+=1
else:
    print("Oops! That's Not Quite Right....")
answer=input("Which Computer program converts assembly language to machine language?\nOptions\n(a)Preprocessor\n(b)Compiler\n(c)Linker\n(d)Assembler\nEnter Your Option:")
if answer.lower()=="d":
    print('You are Quite Right!!!!')
    score+=1
else:
    print("Oh! No,You're Mistaken....")
answer=input("A folder in windows computer can't be made with the name\nOptions\n(a)can\n(b)con\n(c)mak\n(d)make\nEnter Your Option:")
if answer.lower()=="b":
    print('Wow!You Got it....')
    score+=1
else:
    print("No,You've Got it Wrong....")
answer=input("What is the maximum size of a word document creates?\noptions\n(a)64MB\n(b)2GB\n(c)64KB\n(d)32MB\nEnter Your Option:")
if answer.lower()=="d":
    print("That's Spot On!!!!")
    score+=1
else:
    print("I don't Think So....")
if score<3:
    print("Good Try!!")
if score==3:
    print("You're on the right track,Keep Going....")
if score==4:
    print("You're one step closer to Victory....")
if score==5:
    print("Excellent!!!! You did that very well....")


print("You Got " +str(score)+ "Scores")
