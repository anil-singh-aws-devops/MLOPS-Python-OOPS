class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.logged_in=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome to chatbook!! How would you like to proceed
                            1. signup
                            2. signin
                            3. write a post
                            4. message a friend
                            5. Exit\n""")
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            self.write_post()
        elif user_input=='4':
            self.message_friend()
        else:
            print("Exiting the application")
            exit()

    def signup(self):
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        self.username=email
        self.password=password
        print(f"Welcome {self.username}!! You are logged in successfully")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please login to your account")
        else:
            email=input("Enter your email: ")
            password=input("Enter your password: ")
            if self.username==email and self.password==password:
                print("You are logged in successfully")
                self.logged_in=True
            else:
                print("Invalid credentials. Please try again.")
        print("\n")
        self.menu()
    
    def write_post(self):
        if self.logged_in:
            post=input("Write your post: ")
            print(f"Your post '{post}' has been published successfully")
        else:
            print("Please login to your account to write a post")
        self.menu()

    def message_friend(self):
        if self.logged_in:
            friend=input("Enter your friend's email: ")
            message=input("Enter your message: ")
            print(f"Your message '{message}' has been sent to {friend} successfully")
        else:
            print("Please login to your account to message a friend")
        self.menu()

user1=chatbook()