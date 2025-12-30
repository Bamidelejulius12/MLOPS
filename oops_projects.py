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
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
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
            self.menu()
        else:
            username = input("Enter your email / username: ")
            password = input("Enter your password: ")
            if self.username == username and self.password == password:
                print("You have logged in successfully!!")
                self.logged_in = True
                self.menu()
            else:
                print("Invalid credentials. Please input correct credentials.")
    
    def my_post(self):
        if self.logged_in == True:
            text = input(" what's on your mind.. Enter your post here:")
            print(f"following content has been posted -> {text}")
        else:
            print("You need to login first to post something")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.logged_in == True:
            txt = input("Enter your message: ")
            friend = input("whom do you want to send the message to?: ")
            print(f"Your message has been sent to {friend}")
        else:
            print("You need to login first to send messages")
        print("\n")
        self.menu()


obj = chatbook()

