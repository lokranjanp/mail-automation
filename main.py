import smtplib
from email.mime.text import MIMEText

# Set up your email and password
email_address = "lokranjan03@gmail.com"
password = "Lokranjan@03"

# Set up the recipient email address
recipient_email = today_mail

# Create the email content
subject = "Hello from Python!"
body = (f"My heartiest birthday wishes to you, {name}. May god bless you with happiness and success in all your "
        f"endeavours. My best wishes to you. "
        f"Regards,"
        f"Lokranjan")

# Connect to the SMTP server
server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()

# Log in to your email account
server.login(email_address, password)

# Create the email message
message = MIMEText(body)
message["Subject"] = subject
message["From"] = email_address
message["To"] = recipient_email

# Send the email
server.sendmail(email_address, recipient_email, message.as_string())

# Quit the server
server.quit()
