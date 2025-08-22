import random
import math
import smtplib

digits="0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your otp"
msg=OTP

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("saisuryarajanala63@gmail.com","ypfq xpzq xwax cquh")
user="saisuryarajanala63@gmail.com"
mail=input("enter the mail which you want to send opt")
s.sendmail(user,mail,msg)
while True:
    a=input("enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("failure,worng otp")

