import datetime
import smtplib
import random

# To send an email every monday, taking a random quote from the quotes.txt file

current_day = datetime.datetime.now().weekday()

if current_day == 5:  # monday = 0
    with open("quotes.txt") as f:
        all_quotes = f.readlines()  # a list of all quotes
        random_quote = random.choice(all_quotes)  # a random quote

    # send an email with this random quote
    with smtplib.SMTP("smtp.gmail,com") as connection:
        connection.starttls()
        connection.login("email@gmail.com", "password")
        connection.sendmail(
            from_addr="email@gmail.com",
            to_addrs="email2@gmail.com",
            msg=f"Subject: Monday Quote\n\n{random_quote}"
        )
