import random
def passwordgenerator():
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    symbols="!@#$%^&*()_-[]{}"
    combined=lower+upper+numbers+symbols
    length=int(input("Enter The Length Of Password : "))
    password="".join(random.sample(combined,length))
    print("Password : ",password)
def otp():
    numbers="0123456789"
    length=int(input("Enter The Length of OTP : "))
    otp="".join(random.sample(numbers,length))
    print("OTP : ",otp)
print("Choose Any One Option : \n\n1.)Generate a Password\n2.)Generate an OTP\n")
option=int(input("Your Option : "))
if(option==1):
    passwordgenerator()
elif(option==2):
    otp()
else:
    print("Please Enter A Valid Option.")
