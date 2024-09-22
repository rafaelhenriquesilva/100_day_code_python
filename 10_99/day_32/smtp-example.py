# https://support.google.com/mail/thread/205453566/how-to-generate-an-app-password?hl=en
from smtplib import SMTP

origin_email = 'origin_email@gmail.com'
# Generate origin_email to App
password = 'your_app_password'
# SMTP VARIETY
with SMTP('smtp.gmail.com', 587) as connection:

    # Create connection
    connection.starttls()
    connection.login(user=origin_email, password=password)

    connection.sendmail(from_addr=origin_email, to_addrs='destiny_email@gmail.com', msg="Subject: Python email 2 \n\nTest python email 2")
    connection.close()