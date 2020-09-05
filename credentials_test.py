import unittest #Importing unittest module
from credentials import Credentials #importing credentials class

class TestCredentials(unittest.TestCase):
    '''
    creating test cases for credentials class
    '''
    def setUp(self):
        '''
        set up method before test cases
        '''

        self.new_credentials = Credentials("Instagram","paSwo678")
    
    def test_init(self):

        self.assertEqual(self.new_credentials.accountname,"Instagram")
        self.assertEqual(self.new_credentials.accountpassword,"paSwo678")

    def test_save_credentials(self):
        '''
        checks whether the credentials has been saved to credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.cred_list),1)

if __name__ == '__main__':
    unittest.main()