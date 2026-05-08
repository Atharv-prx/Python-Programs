questions = ("1. What is the colour of pikachu?;",
             "2. What is the colour of charmander?",
             "3. What is the colour of bulbasaur?")

options = (("a. Yellow", "b. Orange", "c. Green", "d. Blue"),
            ("a. Orange", "b. Yellow", "c. Green", "d. Blue"),
            ("a. Yellow", "b. Orange", "c. Blue", "d. Green"))

question_num=0
answers = ("a", "a", "d")
guesses = []
score=0


for x in questions:
    print(x)
    for y in options[question_num]:
        print(y)
    guess = input("Enter (a,b,c,d)").lower()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")    
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()    
print(f"Your score is {score} out 3")    