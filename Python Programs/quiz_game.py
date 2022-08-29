from tkinter.messagebox import YES


print("Welcome to my computer quiz challenge ")

playing = input("Do you want to play? ")
score = 0

if playing.lower() == "yes":
    print("Okay let's play ")
else:
    quit()

answer = input("When was the first computer invented? ")
if answer.lower() == "1943":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "Power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("")

print("Your score is "+ str(score)+ " out of 5 questions")
print("You have scored "+ str((score/5)*100)+"%")