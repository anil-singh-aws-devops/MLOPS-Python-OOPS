class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.logged_in=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome to chatbook!! How would you like to proceed
                            1. Login
                            2. Logout
                            3. write a post
                            4. message a friend
                            5. Exit\n""")
        if user_input=='1':
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            print("Exiting the application")
            exit()

object=chatbook()