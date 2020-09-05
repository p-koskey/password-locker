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
