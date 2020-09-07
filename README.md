# Password Locker
This is python application that runs in the terminal. It enables the user to create and login to their account in which they can be able to store and view credentials (account name and password). Users can also delete credentials they no longer require and also copy passwords.

## User Stories
User would like to: 
- create a password locker account with their details, a login username and password.
- store their already existing account credentials in the application.
- create new account credentials in the application. 
- have the option of putting in a password that they want to use for the new credential account.
- view their various account credentials and their passwords in the application.
- delete a credentials account that they no longer need in the application.

## Technologies Used:
-Python 3.8

-Pyperclip

-xsel

## How it works:
Open the Password-Locker folder in the terminal

In the terminal enter command **./run.py**

You'll get a list of short codes to help you navigate the user account:
- Use **nw** - sign up an account, 
- Use **sn**- sign in to your account, 
- Use **ex** -exit Password Locker

After creating a account and successfully signing in, you'll get another list of short codes to help you navigate the credentials account:

- Use **cr**- create new credential account,
- Use **vw** - view existing accounts, 
- Use **fn** - find credentials,
- Use **del**- delete credential account,
- Use **copy** -  copy account password
- Use **ex** - exist password locker
