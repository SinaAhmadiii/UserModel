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
    
    