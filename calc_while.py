print("\nWelcome to the calculator app!")

add = 'addition'
sub = 'subtraction'
div = 'division'
mult = 'multiplication'

while True:
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
        except ValueError as e:
            print("Please enter the numbers. Try again.\n")
            continue
        break

    while True:
        try:
            print(f"\nPlease select a mathematical operation:"
                  f"\n1 - {add}"
                  f"\n2 - {sub}"
                  f"\n3 - {div}"
                  f"\n4 - {mult}"
                  "\n")
            operation = int(input("Enter '1', '2', '3' or '4': "))
        except ValueError or NameError as e:
            continue

        if operation == 1:
            result = first_number + second_number
            print(f"\nYou choose {add}!\nResult is : {result} \n")
            break

        if operation == 2:
            result = first_number - second_number
            print(f"\nYou choose {sub}!\nResult is : {result} \n")
            break

        if operation == 3:
            try:
                result = first_number / second_number
                print(f"\nYou choose {div}!\nResult is : {result} \n")
                break
            except ZeroDivisionError as e:
                print("Division by zero is prohibited.\n")
                break

        if operation == 4:
            result = first_number * second_number
            print(f"\nYou choose {mult}!\nResult is : {result} \n")
            break

    while True:
        try:
            user_input = int(input(f"Do you want continue?"
                                   f"\n1 - 'Yes' 2 - 'No' "
                                   f"\nEnter '1' or '2': "))
        except ValueError or NameError as e:
            print("\nPlease enter '1' or '2'\n")
            continue
        if user_input == 1:
            print(f"\n"
                  f"Great! One more task.")
            break
        if user_input == 2:
            print(f"\n"
                  f"Thanks for using our program!")
            exit()
        else:
            print(f"\nPlease enter '1' or '2'\n")
