import smtplib

mailFrom = "Automatic proccesing"
user = "rafalmizera11@gmail.com"
mailTo = "rafalmizera11@gmail.com"

mailSubject = "Test message from Python"
mailBody = """This is my first message sent from Python.

Have a nice day bro!!!"""

message = f"""mail from: {user}
Subject:{mailSubject}

{mailBody}

Kind regards, RMZ"""

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(user,"TU WPISZ HASŁO")
    server.sendmail(user,mailTo,message)
    server.close()
    print("Email sent succesfully!!!")
except:
    print("Something gone wrong...")