#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

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

def main():
     print("Hello Welcome to Password Locker")
    
     while True:
            print("Use these short codes : nw - sign up an account, ac- sign in to your account, ex -exit Password Lockernew ")
            shortCode = input().lower().strip()
            
            if shortCode == "nw" :
                print("New User")
                print("-"*10)
                print("\n")
                username = input("Enter new Username: ")
                password = input("Enter new password: ")
                
                save_user(create_user(username,password)) #create and save new user
                print("\n")
                print(f"Hello {username} Your user account has been created successfully")
                print("\n")
                print("You can now login to your account... ")

            elif shortCode == "ac":
                print(" Please enter your name and password:")
                print("-"*10)
                print("\n")

                username = input("Username: ")
                password = input("Password: ")

                exists = check_user(username, password)

                if exists:
                    print("\n")
                    print(f"Hi!{username} Welcome back to your account what do you want to do today?")
                    print("Use this short codes to let me know: cr- create new credential account, vw - view existing accounts, del- delete credential account")
                else:
                    print("User doesnt't exist, please try to login again")
if __name__ == '__main__':

    main()
