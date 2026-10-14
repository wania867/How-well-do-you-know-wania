print("💗 HOW WELL DO YOU KNOW ME? 💗")
print("Answer these questions and find out!")

score = 0

answer = input("What is my favourite colour? ")

if answer.lower() == "red":
    print("Correct! You know me!")
    score = score + 1
else:
    print("Wrong answer! 😂")

answer = input("Am I an introvert or extrovert? ")

if answer.lower() == "introvert":
    print("You got it!")
    score = score + 1
else:
    print("Nope! 😂")
    
answer =input("how am i feeling right now")
if answer.lower() == "Happy":
    print("correct! you know me!")
    score=score +1
else:
    print("noooo")
    
answer = input("am i the best daughter in the world?")
if answer.lower() == "yes":
    print("awww i knew it")
    score=score +1


print("Your final score is:", score, "out of 5")