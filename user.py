class User:
    """A class that representing a user

       args:
       username: The username of  the user
       password: The password of the user
       phone_number: The phone number of the user 

    """
    def __init__(self,username:str,password:str,phone_number:str = None) -> None:
        """
            Define a new user 

        Args:
            username (str): The username of user
            password (str): the password of user
            phone_number (str, optional): the phone number of user
        """
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.id = None


    def __str__(self) -> str:
        """
        Return a string representation of user    
        Returns:
            str: string representation of user
        """
        return f"Username : {self.username}\nPhone Number : {self.phone_number}"
    
    @staticmethod
    def validate_password(password:str) -> bool:
        """
        validate the password

        Args:
            password (str): the password to validate

        Returns:
            bool: True if the password is valid, false if password is not valid
        """
        return len(password) >= 4
    
    @property
    def password(self) -> str:
        """
        Get the password of the user
        Returns:
            str: The password of the user
        """
        return self._password
    
    @password.setter
    def password(self,new_password:str) -> None:
        """
        Set the password of the user
        Args:
            new_password (str): the new password to set

        Raises:
            ValueError: if the password is not valid
        """
        if User.validate_password(new_password):
            self._password = new_password
        else:
            raise ValueError("Password must have as least 4 characters")