password = "balaji@786"

password_length = len(password)

print(password_length)

if password_length >= 10:
    password_type = "Strong"
elif password_length >=8 :
    password_type = "Medium"
elif password_length <= 6:
    password_type = "Weak"

print("Password strength is \"",password_type,"\"")