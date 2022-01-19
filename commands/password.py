from cryptography.fernet import Fernet
from require.Text import color, style

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input(color["yellow"] + "What's the master password? " + color["end"])
key = load_key() + master_pwd.encode()
fer = Fernet(key)




def view():
    with open('passwords.txt', 'r') as f:
        print(color["cyan"] + "╭" + "—"*100 + "╮" + color["end"])
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|>")
            text = color["cyan"] + "│ " + color["end"] + color["green"] + user + color["end"] + " — " + color["purple"] + fer.decrypt(passw.encode()).decode()+ color["end"]
            length = 127 - len(text)
            rtext = text + " "*length + color["cyan"] + " │" + color["end"]
            print(rtext)
        print(color["cyan"] + "╰" + "—"*100 + "╯" + color["end"])

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|>" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue