import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "pragatikumari2122@yahoo.com"
PASSWORD ="cvxjiblrpyzajzmp"
PLACEHOLDER = "[NAME]"

today_tuple = (dt.datetime.now().month,dt.datetime.now().day)
data = pandas.read_csv("Day 032\\Birthday Wisher\\birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"Day 032\Birthday Wisher\letter_templates\letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACEHOLDER,birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com",port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )