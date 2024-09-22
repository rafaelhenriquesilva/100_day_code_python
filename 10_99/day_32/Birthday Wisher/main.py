# https://support.google.com/mail/thread/205453566/how-to-generate-an-app-password?hl=en
from smtplib import SMTP
import datetime
from pathlib import Path
import random
EMAIL_EXTENSION = 'gmail.com'
def send_email(origin_email: str, destiny_email: str, subject: str, content: str):
    # SMTP VARIETY
    with SMTP(f'smtp.{EMAIL_EXTENSION}', 587) as connection:

        # Create connection
        connection.starttls()
        connection.login(user=origin_email, password=password)

        connection.sendmail(from_addr=origin_email, to_addrs=destiny_email, msg=f"Subject: {subject}\n\n {content}")
        connection.close()

file_path = Path(__file__).parent / "quotes.txt"
origin_email = f'origin_email@{EMAIL_EXTENSION}'
# Generate email to App
password = 'secret_password'

now = datetime.datetime.now()
day_of_week = now.strftime("%A")
title = f'{day_of_week} Morning'

with open(file_path)  as file:
    all_quotes = file.readlines()
    message_random = random.choice(all_quotes)
    send_email(
        origin_email=origin_email,
        destiny_email=f'destiny_email@{EMAIL_EXTENSION}',
        subject = title,
        content = message_random
    )

