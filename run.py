#!/usr/bin/env python3.6
from password import Password


def create_password(fname, lname, password):

    new_password = Password(fname, lname, password)
    return new_password


def save_passwords(password):

    password.save_password()


def del_password(password):

    password.delete_password()


def find_password(number):

    return Password.find_by_number(number)


def check_existing_passwords(number):

    return Password.password_exist(number)


def display_passwords():

    return Password.display_passwords()


def main():
    print("Hello Welcome to your password-locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new password, dc - display password, fc -find a password, ex -exit the password-locker ")

            short_code = input().lower()

            if short_code == 'cc':
                print("New Password")
                print("-"*10)

                print("First name ....")
                f_name = input()

                print("Last name ...")
                l_name = input()

                print("Password ...")
                password = input()

                

                # create and save new password.
                save_passwords(create_password(
                    f_name, l_name, password))
                print('\n')
                print(f"New Password {f_name} {l_name} created")
                print('\n')

            elif short_code == 'dc':

                if display_passwords():
                    print("Here is a list of all your passwords")
                    print('\n')

                    for password in display_passwords():
                        print(
                            f"{password.first_name} {password.last_name} .....{password.password}")

                    print('\n')
                else:
                    print('\n')
                    print("You don't seem to have any passwords saved yet")
                    print('\n')

            elif short_code == 'fc':

                print("Enter the password you want to search for")

                search_number = input()
                if check_existing_passwords(search_number):
                    search_password = find_password(search_number)
                    print(f"{search_password.first_name} {search_password.last_name}")
                    print('-' * 20)

                    print(f"Password.......{search_password.password}")
                    
                else:
                    print("That password does not exist")

            elif short_code == "ex":
                print("Bye .......")
                break
            else:
                print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
