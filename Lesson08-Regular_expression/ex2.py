import re

class AuthSystem:
    
    def __init__(self):
        """Define regex"""
        self.username_regex = re.compile(r'(?P<Username>[A-Z][a-z]{2})') #如何判斷姓名的正規表示式
        self.password_regex = re.compile(r'(?P<Password>[a-z]{3}[0][0-9]{5})')
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None:
            print("Correct username")
            return True
        else: 
            print("Wrong username")
            return False
        
    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            print("Correct password")
            return True
        else:
            print("Wrong password")
            return False
        
    def authenticate(self, username, password):
        """authenticate the user"""
        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Valid user")

    
# Construct a object of type AuthSystem
auth = AuthSystem()
username=input("Username is:")
password=input("Password is:")

# authenticate the user's credentials
auth.authenticate(username,password)