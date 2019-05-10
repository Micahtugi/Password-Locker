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


if __name__ == '__main__':
    unittest.main()