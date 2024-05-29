from database import Database
from mail_sender import EmailSender

def create_email_body(name, closeness_factor):
    if closeness_factor > 7:
        return (f"My heartiest birthday wishes to you, {name}. May god bless you with happiness and success in all your "
                f"endeavours. My best wishes to you. "
                f"\nRegards,\nLokranjan")
    else:
        return f"Happy Birthday, {name}! Have a great day!\n\nRegards,\nLokranjan"

def main():
    print("Starting the automatic birthday wisher script....\n")
    try:
        db = Database()
        print("Database Connection established")
    except Exception as e:
        print(f"Failed to connect to database : {e}")
        return

    try:
        print("came here")
        email_sender = EmailSender()
        print("Email sender initialised")
    except Exception as e:
        print(f"Failed to initialise email sender : {e}")
        return

    try:
        friends = db.get_birthdays_today()
        print(f"Found {len(friends)} friends with birthdays today")
        if len(friends) == 0:
            print("No Birthday's found for today!")
    except Exception as e:
        print("Error fetching birthdays")
        email_sender.close()
        db.close()
        return

    for friend in friends:
        name, email, closeness_factor = friend
        subject = "Happy Birthday!"
        body = create_email_body(name, closeness_factor)
        try:
            email_sender.send_email(email, subject, body)
            print(f"Sent mail to {name} ({email}).")
        except Exception as e:
            print(f"Failed to send email to {name} ({email}) : {e}")

    email_sender.close()
    db.close()
    print("Finished today's work")

if __name__ == "__main__":
    main()
