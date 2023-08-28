import smtplib
import os


MY_EMAIL = os.environ.get('EMAIL_KEY')
MY_PASSWORD = os.environ.get("PASSWORD_KEY")


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        message = f"Subject:New Response from Void Blog\n\n" \
                  f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        connection.starttls()
        connection.login(user=MY_EMAIL,
                         password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=message)
