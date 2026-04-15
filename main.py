secret_number=35
print("welcome to the game of guesing the number:!!")
print("Guess the number correctly between 1 to 100")


for i in range(1,9):
    try:
        user_input=int(input("enter the number corectly"))
        if user_input <1 or user_input >100:
            print("invalid number!!")
        elif user_input > secret_number:
            print("your number is higher")
        elif user_input < secret_number:
            print("your number is lesser")
        else:
            print("yoour guessed number is correct!! WINNER")
            break
    except ValueError:
        print("invalid charcters,numbers only try again")
    
if secret_number== user_input:
    print(f"Congratulation,you have guessed number{secret_number} in {i} attempts")
else:
    print("Sorrry 🥂. Try agaim!")