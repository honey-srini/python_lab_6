def isX (name,pan):
    if (name.isalpha() == 0) or (pan.isalnum() == 0):
        print("Enter valid PAN number")
        return
    else:
        print("Name: ",name,"Pan: ",pan)

name = input('Enter your Name:')
pan = input("Enter your PAN Number:")
isX(name,pan)
