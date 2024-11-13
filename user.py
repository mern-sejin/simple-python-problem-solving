# PROBLEM-4: user validation checker
stored_email = 'abc@gmail.com'
stored_password = 'secret'

user_name = input('Name: ') or 'User'
user_mail = input('Email Address: ')
user_password = input('Password: ')

if user_mail == stored_email and user_password == stored_password:
    print('Welcome back,', user_name)
elif user_mail != stored_email:
    print('Invalid Email Address!')
elif user_password != stored_password:
    print('Wrong Password!')
else:
    print('Invalid User!')