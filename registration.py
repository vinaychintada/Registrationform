def email_check(e):
    
    SpecialChar =[ '!','@','#','$','%','^','&','*','+','-','`','/',',',';',':','_','(',')','[',']','{','}','<','>','?']

    
    if ('@' not in e) or ('.' not in e) or (' ' in e):
        print('''email/username should have "@" and followed by "." ''')
        return False
        
    if (' ' in e):
        print('''email/username should not contain any spaces''')
        return False
        
    if e.count('@')>1:
        print('''email/username should have only one "@"''')
        return False
        
    if e.count('.')>1:
        print('''email/username should have only one "."''')
        return False
        
    if e.index('@') > e.index('.'):
        print(''' "@" should be followed by "." and doesn't contain any spaces''')
        return False
        
    e=e.replace('@',' ')
    e=e.replace('.',' ')
    l=list(map(str,e.split()))
    
    if len(l)<3:
        print('''There should noit be any "." immediate next to "@" ''')
        return False
        
    if  (l[0][0].isdigit()) or (l[0][0] in SpecialChar):
        print('It should not start with number or any special character')
        return False
    return True


def password_check(password):
	
	SpecialChar =[ '!','@','#','$','%','^','&','*','+','-','`','/',',',';',':','_','(',')','[',']','{','}','<','>','?']
	val = True
	
	if len(password) < 5:
		print('length should be at least 5')
		val = False
		
	if len(password) > 16:
		print('length should be not be greater than ')
		val = False
		
	if not any(char.isdigit() for char in password):
		print('Password should have at least one numeral')
		val = False
		
	if not any(char.isupper() for char in password):
		print('Password should have at least one uppercase letter')
		val = False
		
	if not any(char.islower() for char in password):
		print('Password should have at least one lowercase letter')
		val = False
		
	if not any(char in SpecialChar for char in password):
		print('Password should have at least one special character')
		val = False
	if val:
		return val

def Registration():
    db = open("data.txt",'r')
    username = input("Create username/Email: ")
    password = input("Create password: ")
    password1 = input("Confirm password: ")
    if (password != password1):
        print("password does not match")
        Registration()
    user = []
    pwd = []
    for line in db:
        first,second = line.split(",  ")
        second = second.strip()
        user.append(first)
        pwd.append(second)
    dat = dict(zip(user,pwd)) 
    
    if username in user:
        print("username already exists!")
        Registration()
    else:
        if (email_check(username) and password_check(password)):
            db = open("data.txt",'a')
            db.write(username + ",  " + password + "\n")
            print("Successfully Created!")
        else:
            Registration()
    

def Login():
    db = open("data.txt",'r')
    username = input("Enter username/Email: ")
    password = input("Enter password: ")
    user = []
    pwd = []
    for line in db:
        first,second = line.split(",  ")
        second = second.strip()
        user.append(first)
        pwd.append(second)
    dat = dict(zip(user,pwd)) 
    
    if (username in first):
        if dat[username] != password:
            print("Entered Password is incorrect \nForgot Password?")
            ForgetPassword()
        else:
            print("Logged in Succesfully!")
            print("Hi," + username)
    else:
        print("Username doesn't exist\n")
        res = input("Would you like to Register?y/n \n")
        if res == "y":
            Registration()
        elif res == "n":
            print("")
        else:
            print("Choosen response is Invalid")

def ForgetPassword():
    db = open("data.txt",'r')
    username = input("Enter username/Email: ")
    user = []
    pwd = []
    for line in db:
        first,second = line.split(",  ")
        second = second.strip()
        user.append(first)
        pwd.append(second)
    dat = dict(zip(user,pwd)) 
    
    try:
        if (username in first):
            print("Your Password is : " + dat[username])
    except:
        print("Username doesn't exist\nWould you like to re-Enter?")
        res = input("y/n \n")
        if res == "y":
            ForgetPassword()
        elif res == "n":
            print(" ")
        else:
            print("Choosen response is Invalid")
                        
# Main method
def main():
    res = input("Login | SignUp \n")
    if res == "Login":
        Login()
    elif res == "SignUp":
        Registration()
    else:
        print("Choosen response is Invalid")
        main()
		
# Driver Code
if __name__ == '__main__':
	main()
