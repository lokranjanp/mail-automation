import os
from dotenv import load_dotenv
import smtplib

# Load environment variables from .env file
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

def test_smtp_connection():
    try:
        print(f"Connecting to SMTP server {SMTP_SERVER} on port {SMTP_PORT}...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        status, code = server.ehlo()
        print(f"Status : {status} and Code : {code}")
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("SMTP server connection established and login successful.")
        server.quit()
    except Exception as e:
        print(f"Failed to connect to SMTP server: {e}")

if __name__ == "__main__":
    test_smtp_connection()

#
# import os
# from dotenv import load_dotenv
# import smtplib
#
# # Load environment variables from .env file
# load_dotenv()
#
# EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
# SMTP_SERVER = os.getenv("SMTP_SERVER")
# SMTP_PORT = int(os.getenv("SMTP_PORT"))
#
# def test_smtp_connection():
#     try:
#         print(f"Connecting to SMTP server {SMTP_SERVER} on port {SMTP_PORT}...")
#         server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         server.set_debuglevel(1)  # Enable debug output
#         status, code = server.ehlo()
#         print(f"EHLO response: {status}, {code}")
#         server.quit()
#         print("SMTP server connection established successfully.")
#     except smtplib.SMTPConnectError as e:
#         print(f"SMTP connection error: {e}")
#     except smtplib.SMTPAuthenticationError as e:
#         print(f"SMTP authentication error: {e}")
#     except smtplib.SMTPException as e:
#         print(f"SMTP error: {e}")
#     except Exception as e:
#         print(f"Failed to connect to SMTP server: {e}")
#
# if __name__ == "__main__":
#     test_smtp_connection()
#
