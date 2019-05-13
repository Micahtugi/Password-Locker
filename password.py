class Password:
    
    
    

    password_list = [] # Empty password list
 # Init method up here
    def save_password(self):        
        Password.password_list.append(self)

    def delete_password(self):
        Password.password_list.remove(self)
        
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for password in cls.password_list:
            if password.password == number:
                return password
   
    

    def __init__(self,first_name,last_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    @classmethod
    def password_exist(cls,number):
        for password in cls.password_list:
            if password.password == number:
                    return True

        return False
    @classmethod
    def display_passwords(cls):
        '''
        method that returns the password list
        '''
        return cls.password_list