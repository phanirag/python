username = input("what is your name?")
passwd = input("what is your password")

hased_pass = "*" * len(passwd)
print(f"{username}, your password is {hased_pass}")
