import json

def signup():
    f = open("user_details.json","r")
    c =  f.read()
    k = json.loads(c)
    username=input("Enter your name")
    password=input("Set the password")
    password1=input("Re-enter the password")
    if username in k :
        print("username already exist , Restart") 
        signup()
    else:
        if len(password)>=6 and "@" or "#":
                if password==password1:
                    for i in k :
                        if password not in k[i]["password"]:
                            print("Password been confirmed succesfully")  
                            break     
                        else: 
                            print("password already exist, Restart")
                            signup()       
        else:
            print("Make sure your password is at lest 6 letters")
            signup()  
        firstname=input("Enter your firstname")
        lastname=input("Enter your lastname")
        gender= input("Enter your gender")   
        DOB=input("Enter your birth date")
        k[username]={"username":username,"password":password,"firstname":firstname,"lastname":lastname,"gender":gender,"Date-of-birth":DOB}
        with open("user_details.json","w") as write_file:  
            json.dump(k, write_file , indent=4) 
        write_file.close()
        print("signup successfully.") 
def login():
    username_=input("Enter the username")
    password_=input("Enter the password")
    f = open("user_details.json","r")
    c =  f.read()
    k = json.loads(c)
    for i in k:
        if username_== k[i]["username"]:
            if password_== k[i]["password"] :
                print("login successfully")
                print(k[i])
                break
            else:
                print("your password don't match , Restart")
                login()
        elif username_ in k :
            pass
        else:
            print("username doesn't exist, Restart")
            login()
def begin():
    user=input("Signup or Login?")
    if user == "signup":
        signup()
    elif user == "login":
        login()
    else:
        begin()
begin()


  