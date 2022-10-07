import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from time import sleep


while True:
    email = str(input("Enter your email address >>> "))
    if "@" in email:
        break
    else:
        pass

num = []

for i in range(3):
    element = random.randint(1,9)
    num.append(element)

choice01 = int(input("first num >>> "))
choice02 = int(input("second num >>> "))
choice03 = int(input("third num >>> "))

if choice01 == num[0]\
    and choice02 == num[1]\
        and choice03 == num[2]:
            print("Perfect Clear")
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(#니 구글 이메일, #구글 앱 비밀번호)
            msg = MIMEText("You got perfect answers!")
            msg["Subject"] = "Congratulations!! _Lotto_"
            s.sendmail(#니 구글 , email, msg.as_string())
            s.quit()

else:
    print("It's wrong")





