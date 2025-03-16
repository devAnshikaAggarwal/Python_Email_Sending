# Captcha Email Sender

This is a Python program that sends a randomly generated CAPTCHA to multiple recipients using an SMTP server.

## Features
- **Generate CAPTCHA**: Randomly generate a 6-character alphanumeric CAPTCHA.
- **Read Email List**: Retrieve recipient email addresses from a file.
- **Create Email Message**: Format and include the CAPTCHA in the email content.
- **Send Emails via SMTP**: Use Gmail's SMTP server to send emails securely.

## How to Run
1. Ensure you have Python installed (Python 3.x recommended).
2. Install the required libraries (if not already available):
   ```sh
   pip install smtplib
   ```
3. Create a file named `emails.txt` in the same directory and list recipient emails separated by commas.
4. Run the script:
   ```sh
   python captcha_email.py
   ```

## Configuration
- Update the script with your Gmail credentials.
- Enable **Less Secure Apps** or configure **App Passwords** for secure email sending.

## Example Output
```
Generating captcha: A1B2C3
Sending email to example1@gmail.com
Sending email to example2@gmail.com
Email sent successfully
```

## Requirements
- **Python 3.x**
- **Gmail SMTP Server Access**
- **Valid Email List (emails.txt)**
