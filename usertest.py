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

if __name__ == '__main__':
    unittest.main()