import pyperclip
class Credentials:
    """
    Class that generates new instances of credentials.
    """

    cred_list = [] # Empty credentials list
 

    def __init__(self,acc_name,acc_password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            accountname : acc_name
        accountpassword : acc_password
        '''
      

        self.accountname = acc_name
        self.accountpassword = acc_password
     

    def save_credentials(self):

        '''
        save_user method saves user objects into user_list
        '''

        Credentials.cred_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.cred_list.remove(self)

    @classmethod
    def find_by_accountname(cls,acc_name):
        '''
        Method that takes in a accountname and returns a account that matches that name.

        Args:
            accountname: Account name to search for
        Returns :
            Details of account that matches the name.
        '''

        for name in cls.cred_list:
            if name.accountname == acc_name:
                return name
    
    @classmethod
    def credentials_exist(cls,acc_name):
        '''
        Method that checks if a account exists from the credentials list.
        Args:
           accountname : Account name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for name in cls.cred_list:
            if name.accountname == acc_name:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.cred_list
    
    @classmethod
    def copy_password(cls,acc_name):
        account_found = Credentials.find_by_accountname(acc_name)
        pyperclip.copy(account_found.accountpassword)