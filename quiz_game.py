print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower().strip()

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0


def check_answer(user_input, correct_keywords):
    user_input = user_input.lower().strip()
    for keyword in correct_keywords:
        if keyword in user_input:
            return True
        return False

answer = input("What does CPU stand for? ")
if check_answer(answer,["central processing", "central processing unit"]):
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")
    
answer = input("What Does GPU stand for ")
if check_answer(answer,["graphics processing", "graphics processing unit"]):
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")
    
answer = input("What does RAM stand for? ")
if check_answer(answer,["random access memory", "random access meomory"]):
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")
    
answer = input("What does PSU stand for? ")
if check_answer(answer,["power supply", "power supply unit"]):
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")
    
print("You got " + str(score) + " questions correct! ")
print("You got " + str((score/4) * 100) + " %.")
