
#!/usr/bin/python
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("email", "password") #need to fill in password with actual password
msg = "gregorian chant"
server.sendmail("email", "email", msg)
server.quit()

























