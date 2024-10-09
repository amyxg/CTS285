# This program logs in users: students, parents, teachers

def getUsername():
    userName = input("Enter username ID: ")
    if userName.isdigit():
        return userName
    else:
        displayErrorMsg()
    

def getPasswd():
    passwd = input("Enter password: ")
    return passwd

def displayErrorMsg():
    print("Error! input username and/or password does not exist.")
    print("Check spelling again, password is case-sensitive")

def checkValue()

def main():
    userName = getUsername() 
    password = getPasswd()
    


if __name__ == "__main__":
    main()