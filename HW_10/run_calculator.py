"""
Task 1: Make a calculator
Task 2: Wrap it in 'try'
Task 3*: Make your own exception and connect to try/except
"""
from my_exception_check_zero import CheckZero
from class_calculator import Calculator


def main_run():
    """input output function"""
    str_menu = """+===============MENU===============+
| 1: Addition                      |
| 2: Subtraction                   |
| 3: Multiply                      |
| 4: Division                      |
| 5: The remainder of the division |
| 6: Exponentiation                |
| 0: Exit                          | 
+==================================+"""
    # created an instance of the class
    my_cl = Calculator()

    while True:
        print(str_menu)
        try:
            operation = int(input("Select operation: "))
            # checking whether the necessary commands are in the line
            if operation in (0, 1, 2, 3, 4, 5, 6):
                # checking if the user wants to log out
                if operation == 0:
                    print('Goodbye!')
                    break

                # If not then ask fo the input and call appropiate methods
                first_num = input('Enter first number: ')
                second_num = input('Enter second number: ')

                # checking if a number is entered
                if first_num.isdigit() and second_num.isdigit():
                    first_num = float(first_num)
                    second_num = float(second_num)

                    # Add
                    if operation == 1:
                        print(f'{first_num} + {second_num} = '
                              f'{my_cl.add(first_num, second_num)}')
                    # Subtraction
                    elif operation == 2:
                        print(f'{first_num} - {second_num} = '
                              f'{my_cl.sub(first_num, second_num)}')
                    # Multiply
                    elif operation == 3:
                        print(f'{first_num} * {second_num} = '
                              f'{my_cl.mul(first_num, second_num)}')
                    # Divide
                    elif operation == 4:
                        if second_num == 0:
                            # my exception "class CheckZero"
                            raise CheckZero(second_num)
                        else:
                            print(f'{first_num} / {second_num} = '
                                  f'{my_cl.div(first_num, second_num)}')
                    # The remainder of the division
                    elif operation == 5:
                        if second_num == 0:
                            # my exception "class CheckZero"
                            raise CheckZero(second_num)
                        else:
                            print(f'{first_num} % {second_num} = '
                                  f'{my_cl.mod(first_num, second_num)}')
                    # Exponentiation
                    elif operation == 6:
                        print(f'{first_num} ^ {second_num} = '
                              f'{my_cl.pow(first_num, second_num)}')
                else:
                    print('\nInvalid data type!\nTry again!\n')
            else:
                print('\nInvalid operation\nTry again!\n')

        except (KeyboardInterrupt, CheckZero) as e:
            print(e)


main_run()
