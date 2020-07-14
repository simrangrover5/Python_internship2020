
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib,ssl
from getpass import getpass
import os,sys


from_email = "simrangrover5@gmail.com"
to_email = sys.argv[1]
password = os.environ.get("EMAIL_HOST_PASSWORD")

message = MIMEMultipart("alternative")
message["Subject"] = "Test Mail"
message["From"] = from_email
message["To"] = to_email

host = "smtp.gmail.com"
port = 465

content = """
<html>
<body>
    <h1 style='color:red'>Hello everyone I am mail from python script</h1>
    <a href='https://myaccount.google.com/security'>Click on this link for you google security</a>
    <label style='color:coral;font-size:30px'>Have a good day with this flower!!!! </label>
    <img src='https://images.unsplash.com/photo-1464982326199-86f32f81b211?ixlib=rb-1.2.1&w=1000&q=80'>
</body>
</html>
"""

m = MIMEText(content,"html")  #application/html
#MIMEText(content,"plain")

message.attach(m)  #message attach to the MIMEmultipart subject and this message will be send to receiver

context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL(host,port,context=context) as mailserver:
        mailserver.login(from_email,password)
        mailserver.sendmail(from_email,to_email,message.as_string())
except Exception as e:
    print("\n Error ",e)
else:
    print("\n Successfully send the message")
