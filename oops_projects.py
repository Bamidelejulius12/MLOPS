class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()
    
    def menu(self):
        user_input = input(""" Welcome to chatbook! || how would you like to proceed?
                           1. press 1 to Sign Up
                           2. press 2 to login 
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit : """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            print("Thank you for visiting chatbook. Goodbye!")
            exit()

    def signup(self):
        email = input("Enter your email: ")
        password = input("Create a password: ")
        self.username = email
        self.password = password
        print("You have signed up successfully!!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == "" and self.password == "":
            print("you need to sign up first by pressing 1 in the main menu")
        else:
            username = input("Enter your email / username: ")
            password = input("Enter your password: ")
            if self.username == username and self.password == password:
                print("You have logged in successfully!!")
                self.logged_in = True
                self.menu()
            else:
                print("Invalid credentials. Please input correct credentials.")

obj = chatbook()

