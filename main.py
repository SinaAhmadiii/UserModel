from user import User
"""
    This module define the user model class
    
"""

class UserMenu:
    """A class  representing a user menu

    """

    def __init__(self):
        self.users = {}
        self.current_user = None

    def register_user(self) -> None:
        """
           Register a new user by taking information from the user
        """
        
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        phone_number = input("(Optional) Please enter your phone number : ")

        if not self.is_username_valid(username):
            print("Please enter a valid username")
            return
        if not self.is_username_available(username):
            print("Username is already taken")
            return
        if not User.validate_password(password):
            print("password must have at least 4 characters")
            return
        
        user = User(username,password,phone_number)
        self.generate_user_id(user)
        self.users[user.id] = user
        print("user registered successfully")


    def is_username_valid(self,username: str) -> bool:
        """
            Check the username is valid
            args:
                username (str): the Username to check
            Returns:
                bool: True if the username is valid or false if username is not valid

        """        
        return len(username) > 0
    

    def is_username_available(self,username: str) -> bool:
        """
        check the username for registration

        Args:
            username (str): the username for check

        Returns:
            bool: True if username is available , if not is False

        """
        for user in self.users.values():
            if user.username == username:
                return False
        return True
    
    def generate_user_id(self,user: User) -> None:
        """
        Generate a unique ID

        Args:
            user (User): the user to generate
        """
        user.id = len(self.users) + 1


    def login_user(self) -> None:
        """
            Log in the system with valid username and password        
        """
        username = input("Please Enter your username : ")
        password = input("Please enter your password : ")

        for user in self.users.values():
            if user.username == username and user.password == password:
                self.current_user = user
                print("Login successful")
                return

        print("Incorrect username or password")

    def logout_user(self) -> None:
        """
            Log out the username 
        """
        self.current_user = None
        print("logged out successfully")

    def change_password(self) -> None:
        """
           change the password of username
        """
        if self.current_user:
            old_password = input("Please enter your old password : ")
            new_password = input("Please enter your new password : ")
            confirm_password = input("Confirm your new password : ")

            if old_password != self.current_user.password:
                print("incorrect old password")
                return
            if new_password != confirm_password:
                print("new password and confirm password do not match")
                return
            if not User.validate_password(new_password):
                print("password must have at least 4 characters")
                return
            
            self.current_user.password = new_password
            print("Password changed successfully")
        else:
              print("You are not logged in ")

    def edit_user_info(self) -> None:
        """
           edit the information of user
        """
        if self.current_user:
            new_username = input("Please enter your new Username : ")
            new_phone_number = input("Please enter your new phone number : ")

            if not self.is_username_valid(new_username):
                print("Please Enter a valid username")
                return
            if not self.is_username_available(new_username) and new_username != self.current_user.username:
                print("username is already taken . ")
                return
        
            self.current_user.username = new_username
            self.current_user.phone_number = new_phone_number
            print("User information updated")
        else:
            print("you are not logged in")

menu = UserMenu()

while True:
    print("1. Register User")
    print("2. Login user")
    print("3. Change password ")
    print("4. Edit user information")
    print("0 . Exit")
    option = input("Please Enter your choice : ")

    if option == "0":
        break
    elif option == "1":
        menu.register_user()
    elif option == "2":
        menu.login_user()
    elif option == "3":
        menu.change_password()
    elif option == "4":
        menu.edit_user_info()
    else:
        print("Invalid option.Please try again")
    

        