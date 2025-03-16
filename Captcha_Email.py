# Write a function based program to send a captcha email to multiple recipients using SMTP server.

import smtplib
import random
import string

# Captcha generation
def generate_captcha():
    captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return captcha

# Email data
def get_email_data():
    try:
        with open("./emails.txt", "r") as file:
            email_data = file.read().strip().split(",")
            print(email_data)
        return email_data
    except FileNotFoundError:
        print("File not found")
        return []

# Message
def create_message():
    captcha = generate_captcha()
    print(f"Generating captcha: {captcha}")
    message = f"Subject: Captcha\n\nYour captcha is {captcha}"
    return message

# Email sending
def send_email(email_data):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("2005anshi1089ind@gmail.com", "tsbd iznv uysf uwmt")
        message = create_message()
        for email in email_data:
            server.sendmail("2005anshi1089ind@gmail.com", email, message)
            print(f"Sending email to {email}")
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Email not sent: {e}")

# Main
def main():
    email_data = get_email_data()
    if email_data:
        send_email(email_data)

if __name__ == "__main__":
    main()