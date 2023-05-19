class User:
    """A class that representing a user

       args:
       username: The username of  the user
       password: The password of the user
       phone_number: The phone number of the user 

    """
    def __init__(self,username:str,password:str,phone_number:str = None) -> None:
    
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.id = None


    def __str__(self) -> str:
        return f"Username : {self.username}\nPhone Number : {self.phone_number}"
    
    @staticmethod
    def validate_password(password:str) -> bool:

        return len(password) >= 4
    
    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self,new_password:str) -> None:

        if User.validate_password(new_password):
            self._password = new_password
        else:
            raise ValueError("Password must have as least 4 characters")