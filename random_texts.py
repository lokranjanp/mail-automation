import random, time
random.seed(int(time.time()))

def create_mail_body(name):
    text_dict = [f"My heartiest birthday wishes to you, {name}. May god bless you with happiness and success in all your "
                f"endeavours. Best wishes to you. "
                f"\nRegards,\nLokranjan",

                f"Happy Birthday, {name}! Wishing you a day filled with sunshine, laughter, and all the things that make "
                f"your heart sing. Here's to another year of amazing adventures!. Best Wishes <3"
                f"\nRegards, \nLokranjan",

                f"To my dear friend, {name}, Happy Birthday! May your day be overflowing with joy and love. Wishing you"
                f"all the happiness in the world. Best Wishes"
                f"\nRegards, \nLokranjan",

                f"Happy Birthday, {name}!  Here's to celebrating another year of your incredible presence. Your friendship"
                f"brings so much light to my life. Wishing you a day as special as you are. Best Wishes"
                f"\nRegards, \nLokranjan",

                f"Sending you the warmest birthday wishes, {name}!  May this year bring you countless reasons to smile and"
                f"unforgettable memories to cherish. Happy Birthday!"
                f"\nRegards, \nLokranjan",

                f"Happy Birthday, {name}!  So grateful to have you in my life. Wishing you a day filled with laughter, "
                f"love, and all the best things. Cheers to another year of friendship!"
                f"\nRegards, \nLokranjan"]

    return random.choice(text_dict)
