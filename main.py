import random

'''
This algorithm solves the problem of getting a password for the user.
Returns a random password with a collection of letter and numbers
Also adds random characters at the request of the user
'''


def main():
    print('--------------------------------------------------')
    print('This program generates a random password for you.')
    print('--------------------------------------------------')

    # User choices are recorded to variable "choices" as a list
    # Then the list values are sent into the random_password function as arguments
    choices = user_choices()
    choice_numbers = choices[0]
    choice_letters = choices[1]
    choice_special = choices[2]

    password = random_password(choice_numbers, choice_letters, choice_special)

    # Outputs your random password
    print('')
    print('Here is your password: ' + str(password))
    print(' ')


    # Function allows user to save generated passwords to a text file
    while True:
        save_password = input("Do you want to save password? ( 1 for Yes OR 2 for No): ")
        if save_password.isdecimal():
            save_password = int(save_password)
            if save_password == 1:
                print("Password will be saved. Check the passwords folder.")
                save(password)
                break
            elif save_password == 2:
                print("Password will not be saved.")
                break
            else:
                print("Choice is invalid. Try Again.")


def random_password(choice_numbers, choice_letters, choice_special):
    '''
    Generate a random password to be returned to the user.
    Password should include a combination of letters and numbers.
    '''

    # Step 1: Get the random numbers
    # Random numbers refers to a number between the range of (0 to 9999)
    random_numbers = ''

    for i in range(choice_numbers):
        number = random.randint(0, 9)
        random_numbers = random_numbers + str(number)

    # Step 2: Get the random letters
    # Random Letters refers to letters that the password will contain
    # converts "qwertyuiopasdfghjklzxcvbnm"  to a list to pull values

    letters = []
    letters[:0] = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    random_letters = ''

    # Gives a set number of random letters for the password, then combines them 
    for i in range(choice_letters):
        letter = random.choice(letters)
        random_letters = random_letters + letter

    # Step 3: Get random special character for password
    # Random symbols refers to the list of special characters that the password will produce
    # converts "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" to a list to pull values

    symbols = []
    symbols[0:] = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    random_symbols = ''

    # Gives a set number of random symbols for the password, then combines them
    for i in range(choice_special):
        symbol = random.choice(symbols)
        random_symbols = random_symbols + symbol

    # Outputs back the password
    # random.sample() will return one of each value in list
    # takes each character in random_order list and joins to form the password

    random_order = []
    random_order[0:] = (random_letters + random_numbers + random_symbols)
    character = random.sample(random_order, len(random_order))
    password = ''.join(character)
    return password


def user_choices():
    # Gives the user flexibility on the amount of numbers and letters they want in their password
    # Adds an option to include special characters, in case for those password checkers that do not support them

    # Each loop checks the input value, if invalid, asks again for input till a valid one is produced
    while True:
        choice_numbers = input("How many numbers do you want? ")
        if choice_numbers.isdecimal():
            choice_numbers = int(choice_numbers)
            print("Your password will have " + str(choice_numbers) + " numbers.")
            break
        else:
            print("Choice is invalid. Try Again.")
    print('')

    while True:
        choice_letters = input("How many letters do you want? ")
        if choice_letters.isdecimal():
            choice_letters = int(choice_letters)
            print("Your password will have " + str(choice_letters) + " letters.")
            break
        else:
            print("Choice is invalid. Try Again.")
    print('')

    while True:
        choice_special = input("Do you want special characters? (1 for Yes OR 2 for No) ")
        if choice_special.isdecimal():
            choice_special = int(choice_special)
            if choice_special == 1:
                print("Your password will have special characters.")
                choice_special = input("How many do you want? ")
                if choice_special.isdecimal():
                    choice_special = int(choice_special)
                    print("Your password will have " + str(choice_special) + " special characters.")
                    return (choice_numbers, choice_letters, choice_special)
                    break
                else:
                    print("Choice is invalid. Try Again.")
            elif choice_special == 2:
                print("Your password will not have special characters.")
                choice_special = 0
                return (choice_numbers, choice_letters, choice_special)
                break
            else:
                print("Choice is invalid. Try Again.")
        else:
            print("Choice is invalid. Try Again.")
    print('')


'''
This function saves generated passwords
to a text file "passwords" for future reference
'''


def save(password):
    with open("passwords\password.txt", "a") as f:
        f.write(password + "\n")


main()

'''
In random_password(), issue where the position of special characters is not asked, thus should return randomly 
in front or back of password. 
'''

'''
Wanted to add functionality to allow user choice order, but that may reduce password strength as 
well as issues surrounding concatenation with resulting password string 
'''
