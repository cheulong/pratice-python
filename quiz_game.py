print("Welcome to the Quiz Game!")

playing = input("Do you want to play? (y/n) ")

if playing.lower() != "y":
    quit()

print("Ok let's get started!")
score = 0

answer = input("What is CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'central processing unit'.")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'graphics processing unit'.")

answer = input("What is RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'random access memory'.")

print(f"Your score is {score} out of 3")
print(f"Your got {round(score / 3, 2)}%")