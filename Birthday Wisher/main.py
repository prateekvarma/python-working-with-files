# Day 32
import datetime
import random
import smtplib
import pandas

current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
today_tuple = (current_month, current_day)

data_df = pandas.read_csv("birthdays.csv")

# create a dict with pattern like {(month, dat): Test-name,test@email.com,1961,12,21, ...}
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data_df.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("senders-email@gmail.com", "password")
        connection.sendmail(
            from_addr="email@gmail.com",
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
