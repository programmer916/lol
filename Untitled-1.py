master_pwd = input("enter your password: ")

def veiw():
    pass

def add():
    name = input("Account name:")
    pwd = input("Password: ")

    with open('Password.txt' , 'a') as f:
        f.write(name + "" + pwd + "/n")



while True:
    mode = input("Would you like to add a nnew password or view a existing ones (view, add), press q to quit? ").lower()
if mode == "q":
    break

if mode == "view":
    veiw()
if mode == "add":
    add()
else:
    print("invalid mode")
    continue