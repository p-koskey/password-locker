import unittest #Importing unittest module
from credentials import Credentials #importing credentials class
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    creating test cases for credentials class
    '''
    def setUp(self):
        '''
        set up method before test cases
        '''

        self.new_credentials = Credentials("Instagram","paSwo678")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.cred_list = []
    
    def test_init(self):

        self.assertEqual(self.new_credentials.accountname,"Instagram")
        self.assertEqual(self.new_credentials.accountpassword,"paSwo678")

    def test_save_credentials(self):
        '''
        checks whether the credentials has been saved to credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.cred_list),1)

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Twitter","twe458") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.cred_list),2)

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credentials from our credentials list
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials("Netflix","fghjk") # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a credentials object
            self.assertEqual(len(Credentials.cred_list),1)

    def test_find_credentials_by_accountname(self):
        '''
        test to check if we can find an account credentials by name and display password
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","user56789") # new account
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_accountname("Facebook")

        self.assertEqual(found_credentials.accountname,test_credentials.accountname)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Pinterest","23dfgdb") # new account
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Pinterest")

        self.assertTrue(credentials_exists)


    def test_display_all_credentials(self):
        '''
        method that returns a list of all account credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.cred_list)

    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from a found account
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_password("Instagram")

        self.assertEqual(self.new_credentials.accountpassword,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()