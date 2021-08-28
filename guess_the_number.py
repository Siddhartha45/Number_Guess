#guess the number

n = 34
guess = 1

while(guess<=10):

    a = int(input("Guess the number:\n"))

    if a>n:
        print("The entered number is greater. Please try smaller number!")

    elif a==n:
        print("Congractulations! Your guess is correct. You won!")
        print("You guessed the right number in", guess ,"tries.")
        break

    elif a<n:
        print("The entered number is lesser. Please try greater number!")

    print(10 - guess, "no. of guesses left\n")
    guess = guess + 1

    if guess==11:
        print("Sorry! You could not guess the right number in ten tries. The correct number is", n)



