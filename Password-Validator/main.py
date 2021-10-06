import bcrypt

password = b"password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

entered_password = input("Login:")
entered_password = bytes(entered_password, encoding="utf-8")

if bcrypt.checkpw(entered_password, hashed):
    print("Login Successful.")
else:
    print("Invalid password")

