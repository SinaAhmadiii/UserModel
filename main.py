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
    


        