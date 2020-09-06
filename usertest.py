import unittest #Importing unittest module
from user import User #importing user class

class TestUser(unittest.TestCase):
    '''
    creating test cases for user class
    '''
    def setUp(self):
        '''
        set up method before test cases
        '''

        self.new_user = User("Ngugi","paSwo678")
    
    def test_init(self):

        self.assertEqual(self.new_user.username,"Ngugi")
        self.assertEqual(self.new_user.password,"paSwo678")

    def test_save_user(self):
        '''
        checks whether the user has been saved to user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Patience","23dfgdb") # new account
        test_user.save_user()

        user_exists = User.user_exist("Patience","23dfgdb")

        self.assertTrue(user_exists)

if __name__ == '__main__':
    unittest.main()