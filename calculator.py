# This is a calculator made by python

# Welcome message
print("This is a simple calculator made by python. I hope you find it useful.\n")

# Menu options
def help_mssg():
    print("""Please choose a suitable option:\n
    1.) Addition
    2.) Subtraction
    3.) Multiplication
    4.) Division
    5.) Quit\n""")

# Functions

def add(num_1, num_2, sum):
    print(f"\n{num_1} + {num_2} = {sum}\n")

def sub(num_1, num_2, difference):
    print(f"\n{num_1} - {num_2} = {difference}\n")

def mul(num_1, num_2, product):
    print(f"\n{num_1} x {num_2} = {product}\n")

def div(num_1, num_2, quotient):
    print(f"\n{num_1} ÷ {num_2} = {quotient}\n")

while True:
    help_mssg()

    user_choice = input("Which option would you like to choose [1-5]: ")

    if user_choice in ("1","2","3","4"):

        try:
            choice_1 = input("\nChoose your first number: ")
            choice_2 = input("Choose your second number: ")

            sum = (float(choice_1)) + (float(choice_2))
            difference = (float(choice_1)) - (float(choice_2))
            product = (float(choice_1)) * (float(choice_2))
            quotient = (float(choice_1)) / (float(choice_2))

            if user_choice == "1":
                add(choice_1, choice_2, sum)
        
            elif user_choice == "2":
                sub(choice_1, choice_2, difference)
            
            elif user_choice == "3":
                mul(choice_1, choice_2, product)

            elif user_choice == "4":
                div(choice_1, choice_2, quotient)
                            
        except ZeroDivisionError:
            print("! CANNOT DIVIDE BY ZERO !")
        except ValueError:
            print("\n! YOU MUST TYPE IN A NUMBER NOT LETTERS, SYMBOLS, ETC !\n")

    elif user_choice == "5":
        print("\nThank you for using my calculator; hope it was useful :)\n")
        exit()

    else:
        print("\n! INVALID INPUT !\n")