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
        


if __name__ == '__main__':
    unittest.main()