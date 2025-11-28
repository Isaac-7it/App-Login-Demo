class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


print('Welcome!')
running = True
command = input('Create an Account (C) / Login (L) ')
while running:
    if command.lower() == 'create account' or command.lower() == 'c':
        new_username = input('Name ')
        new_user_email = input('Email ')
        new_user_password = input('Enter password ')
        new_user_confirm_password = input('Confirm password ')
        new_user = User(new_username, new_user_email, new_user_password)
        is_email_valid = '@gmail.com' in new_user_email
        # Validating Emails
        # while not is_email_valid:
        #     new_user_email = input('Your Email should end with a domain! Email ')
        #     if '@gmail.com' in new_user_email:
        #         break
        if new_user_confirm_password == new_user_password:
            command = input('Account created! Proceed to Login (L) ')
        while new_user_confirm_password != new_user_password:
            new_user_password = input("Passwords doesn't match! Enter password ")
            new_user_confirm_password = input('Confirm password ')

            if new_user_confirm_password == new_user_password:
                command = input('Account created! Proceed to Login (L) ')
    elif command.lower() == 'login' or command.lower() == 'l':
        try:
            login_email = input('Email ')
            login_password = input('Password ')
            if login_email == new_user.email and login_password == new_user_password:
                print(f'Login Successful! Welcome {new_user.name}')
                running = False
                break
            else:
                # print(login_email, new_user_email)
                # print(login_password, new_user_password)
                print('Wrong Email or Password')
        except NameError:
            command = input("Your account doesn't exist. Create an Account (C) ")
    else:
        command = input('Error! Create an Account (C) / Login (L) ')

