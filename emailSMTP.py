
#!/usr/bin/python
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("emquantum64@gmail.com", "raspberrypi")
msg = "gregorian chant"
server.sendmail("emquantum64@gmail.com", "emthequan@gmail.com", msg)
server.quit()

























