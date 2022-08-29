print('Create an Account')

username = input('Create an Username: ').lower()
password = input('Create a Password: ')

print('Account created successfully!!')
print('Login now!')

username1 = input('Enter your username: ').lower()
password1 = input('Enter your password: ')

if username == username1 and password == password1:
    print('Logged in sucessfully!')
else:
    print('Invalid credentials :(')
