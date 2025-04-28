import art as a
import random as r
num = r.randint(1,100)
print(f"{a.logo} \n Welcome, to the number guessing game! You have to guess the number I'm thinking of between 1 and 100")
difficulty = input("Do you want to keep the game 'easy' or 'hard'? E/H: ").lower()
def guessnum():
    global num
    if difficulty =='e':
        n=10
        print(f"You'll have {n} attempts")
        while n>0:
            guess= int(input("Make a guess: "))
            if guess>num:
                n -= 1

                if n == 0:
                    print("Game Over")
                    break
                print("Guess lower")
                print(f"{n} attempts remaining!")

            elif guess<num:
                n -= 1
                if n == 0:
                    print("Game Over")
                    break
                print("Guess higher")
                print(f"{n} attempts remaining!")

            elif guess == num:
                print("correct")
                print(f"the num was {num}")
                break

    elif difficulty == 'h':
        n = 5
        print(f"You'll have {n} attempts")
        while n > 0:
            guess = int(input("Make a guess: "))
            if guess > num:
                n -= 1
                if n == 0:
                    print("Game Over")
                    break
                print("Guess lower")
                print(f"{n} attempts remaining!")

            elif guess < num:
                n -= 1
                if n == 0:
                    print("Game Over")
                    break
                print("Guess higher")
                print(f"{n} attempts remaining!")

            elif guess == num:
                print("correct")
                print(f"the num was {num}")
                break

    else:
        print("Wrong input!, try again")
guessnum()


