from user import User

class UserMenu:

    def __init__(self):
        self.users = {}
        self.current_user = None

    def register_user(self) -> None:
        
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

        return len(username) > 0
    

    def is_username_available(self,username: str) -> bool:

        for user in self.users.values():
            if user.username == username:
                return False
        return True
    
    def generate_user_id(self,user: User) -> None:
        user.id = len(self.users) + 1


    def login_user(self) -> None:
        username = input("Please Enter your username : ")
        password = input("Please enter your password : ")

        for user in self.users.values():
            if user.username == username and user.password == password:
                self.current_user = user
                print("Login successful")
                return

        print("Incorrect username or password")

    def logout_user(self) -> None:
        self.current_user = None
        print("logged out successfully")

    def change_password(self) -> None:
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

      


    

        