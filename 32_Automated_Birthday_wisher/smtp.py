# sender@gmail.com and recipient@yahoo.com 
# sender ( sender--> Gmail Mail Server --> Yahoo Mail Server --> recipient )

# It relies on SMPT
# SMPT simple mail transfer protocol

import smtplib


my_email = "example@gmail.com"
password = "abcd123"
connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email, to_addrs="destination@gmail.com", msg="Hello Dummy Message")

connection.close()

