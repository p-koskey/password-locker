class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty user list
 

    def __init__(self,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: user's name
            password: user's password
        '''
      

        self.username = username
        self.password = password
     

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
