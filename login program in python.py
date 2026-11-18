users = {"user1": "password1", "user2": "password2"}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users:
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password.")
            forgotpassword()
    else:
        print("Username not found.")
def forgotPassword():
    if username.exists() == true
        print("Update password")
        newPassword = input("Enter your new password : ")
        
# Example usage call the function
login()
