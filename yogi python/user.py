user = "yogi"
password = 1234

enter_user = input("Enter your username: ")
enter_password = int(input("Enter your password: "))

if user == enter_user and password == enter_password:
    print("Login Successful")
    print("Welcome")
else:
    print("Invalid Username or Password")
