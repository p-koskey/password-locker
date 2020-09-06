#!/usr/bin/env python3.8
from user import User
from credentials import Credentials
import random
import string

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)

    return new_user

def save_user(user):
    '''
    function to save user created
    '''
    user.save_user()

def check_user(username,password):
    '''
    function to check whether user account exists
    '''
    return User.user_exist(username,password)

def create_credentials(acc_name,acc_password):
    '''
    Function to create a new account
    '''
    new_cred = Credentials(acc_name, acc_password)

    return new_cred

def save_credentials(credentials):
    '''
    function to save credentials created
    '''
    credentials.save_credentials()
  

def delete_credentials(credentials):
    '''
    function to delete credentials
    '''
    credentials.delete_credentials()

def find_account(acc_name):
    '''
    functiom that find account by name
    '''
    return Credentials.find_by_accountname(acc_name)

def check_existing_account(acc_name):
    '''
    Function that check if an account credentials exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(acc_name)

def display_accounts():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def copy_password(acc_name):
    '''
    Function that handles the behaviour of copy email to the clipboard
    '''
    return Credentials.copy_password(acc_name)

def main():
     print("\n")
     print("Hello! Welcome to PASSWORD LOCKER")
     print("-"*100)
     print("\n")
    
     while True:
            print("Use these short codes : \nnw - sign up an account, \nsn- sign in to your account, \nex -exit Password Locker")
            shortCode = input().lower().strip()
            
            if shortCode == "nw" :
                print("")
                print("-"*100)
                print("NEW USER")
                print("-"*100)
                print("\n")
                username = input("Enter new Username: ")
                password = input("Enter new password: ")
                
                save_user(create_user(username,password)) #create and save new user
                print("\n")
                print(f"Hello {username} Your user account has been created successfully")
                print("\n")
                print("You can now sign in to your account... using short code sn")
                print("-"*100)
                print("\n")

            elif shortCode == "ex":
                print("\n")
                print("Bye!")
                print("-"*100)
                break

            elif shortCode == "sn":
                print("-"*100)
                print(" Please enter your name and password:")
                print("-"*100)
                print("\n")

                username = input("Username: ")
                password = input("Password: ")

                exists = check_user(username, password)

                if exists:
                    
                    print("\n")
                    print(f"Hi! {username} Welcome back to your account!")
                    print("\n")
                    while True:
                            print("Use these short codes :\ncr- create new credential account,\nvw - view existing accounts, \nfn - find credentials,\ndel- delete credential account,\ncopy -  copy account password\nex - exist password locker")
                            print("\n")
                            shortCode = input().lower().strip()
                            if shortCode == "cr" :
                                    print("New Credential")
                                    print("-"*100)
                                    print("\n")
                                    acc_name = input("Enter new account name: ")
                                    print("\n")
                                    while True:
                                        print("gn - if you'd like to generate a password, cs- if you'd like to create your own password")
                                        key = input()
                                        if key == "gn":
                                            print("\n")
                                            print('Please enter password length: ')
                                            n = int(input())#password length
                                            #allowed string constants
                                            chars = string.ascii_letters + string.digits + string.punctuation
                                            #generate password
                                            password = ''.join(random.choice(chars) for _ in range(n))

                                            acc_password = password
                                            print("\n")
                                            print('Your account password has been created successfully')
                                            print("-"*100)
                                            
                                        elif key == "cs" :
                                            print("\n")
                                            acc_password = input("Enter new account password: ")
                                            
                                        else:
                                            print("\n")
                                            print("I really didn't get that. Please use the correct short codes")
                                            print("-"*100)
                                            break
                                        
                                    save_credentials(create_credentials(acc_name,acc_password)) #create and save new account
                                    print("\n")
                                    print(f"Your credential account {acc_name} has been created successfully")
                                    print("-"*100)
                            elif shortCode == "vw":

                                    if display_accounts():
                                            print("\n")
                                            print("Here is a list of all your credentials")
                                            print("-"*100)
                                            print('\n')

                                            for credential in display_accounts():
                                                    print(f"{credential.accountname}: {credential.accountpassword} ")

                                            print('\n')
                                    else:
                                            print('\n')
                                            print("You dont seem to have any accounts saved yet")
                                            print("-"*100)
                            elif shortCode == 'fn':

                                    print("Enter the account name you want to search for")

                                    search_account = input()
                                    if check_existing_account(search_account):
                                            find = find_account(search_account)
                                            print("\n")
                                            print(f"{find.accountname} : {find.accountpassword}")
                                            print('-' * 100)
                                    else:
                                            print("\n")
                                            print("That account  does not exist")
                                            print("-"*100)
                
                else:
                    print("\n")
                    print("User doesnt't exist, please try to login again or create new account")
                    print("-"*100)
            
            else:
                print("\n")
                print("I really didn't get that. Please use the short codes")
                print("-"*100)
     

if __name__ == '__main__':

    main()
