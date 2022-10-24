import smtplib

sender = "arkadiuszmazurek13@gmail.com"
receiver = "feniksfeve@gmail.com"
password = "kjkzszgqnsbzbsbx"
subject = "Python sie odzywa"
body = "Masz maila"


message = f"""From : {sender}
To: {receiver}
Subject: {subject} \n
{body}
"""

print("Start: ")
server = smtplib.SMTP("smtp.gmail.com", 587)

print("Server connected ")
server.starttls()

print("Login start ")
server.login(sender, password)
print("Logged in...")

server.sendmail(sender, receiver, message)
print("Email has been sent!")

