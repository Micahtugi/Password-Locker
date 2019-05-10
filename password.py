class Password:
    """
    Class that generates new instances of passwords.
    """

    password_list = [] # Empty password list

    def __init__(self,first_name,last_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        