import unittest # Importing the unittest module
from password import Password # Importing the password class

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password("Micah","Mutugi","python") # create password object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"Micah")
        self.assertEqual(self.new_password.last_name,"Mutugi")
        self.assertEqual(self.new_password.password,"python")
    def test_save_password(self):
        '''
        test_save_password test case to test if the password object is saved into
         the password list
        '''
        self.new_password.save_password() # saving the new password
        self.assertEqual(len(Password.password_list),1) 
    def test_save_multiple_password(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our password_list
            '''
            self.new_password.save_password()
            test_password = Password("Test","user","python") # new password
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Password.password_list = []
    def test_save_multiple_password(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our password_list
            '''
            self.new_password.save_password()
            test_password = Password("Test","user","python") # new password
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)
    def test_delete_password(self):
            '''
            test_delete_password to test if we can remove a password from our password list
            '''
            self.new_password.save_password()
            test_password = Password("Test","user","python") # new password
            test_password.save_password()

            self.new_password.delete_password()# Deleting a password object
            self.assertEqual(len(Password.password_list),1)
    def test_find_password_by_number(self):
        '''
        test to check if we can find a password by phone number and display information
        '''

        self.new_password.save_password()
        test_password = Password("Test","user","python") # new password
        test_password.save_password()

        found_password = Password.find_by_number("python")

        
    
    

if __name__ == '__main__':
    unittest.main()