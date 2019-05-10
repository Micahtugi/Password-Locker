class Password:
    """
    
    """

    password_list = [] # Empty password list
 # Init method up here
    def save_password(self):

        '''
        
        '''

        Password.password_list.append(self)
    def delete_password(self):

        '''
        
        '''

        Password.password_list.remove(self)

    def __init__(self,first_name,last_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        