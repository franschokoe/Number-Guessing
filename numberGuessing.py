import random

# Priject Title 
print()
print('------------NUMBER GUESSING GAME---------------')
print()

keepPlaying = True
# Loop for to continue playing
while keepPlaying:
    # Error Handling
    try:
        # select the range
        num_range = random.randint(1 ,50)
        num_userv= int(input("Guess any number between 1 - 50: "))
        isEveOdd = input("Is the number even or odd ?: ").upper()


        even  = (num_range % 2 == 0)
        odd = (num_range % 2 != 0)

        if num_userv <= 50:
            if num_userv == num_range and even and isEveOdd =='EVEN':
                print()
                print(f"You guessed the correct number [{num_range}]")
                print('The number is Even')
            elif num_userv == num_range and odd and isEveOdd =='ODD':
                print()
                print(f"You guessed the correct number [{num_range}]")
                print("The number is ODD")
            elif num_userv != num_range and even and isEveOdd =='EVEN':
                print()
                print(f'Not a correct guess, [{num_range}] is the rigt number')
                print("The number is Even")
            elif num_userv != num_range and odd and isEveOdd =='ODD':
                print()
                print(f'Not a correct guess, [{num_range}] is the rigt number')
                print("The number is ODD")
            else:
                print()
                print("none - You did  not guess any")

        elif num_userv > 50:
            print()
            print("You are out of the range\nSelect numbers  betweem 1 and 50.")
            break
        
    except ValueError:
        print()
        print("numbers required on then first question")

    user_input = input('Want to proceed [Y,n] ?: ').upper()

    if user_input == 'Y':
        continue
    else :
        break


print("done")







# Developed by Frans Chokoe
# Project info - Name : Number Guessing 
#              - Time : 18:37
#              - Date : 08 July 2025