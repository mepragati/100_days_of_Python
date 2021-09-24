import smtplib
import datetime as dt
import random

MY_EMAIL = "pragatitesting@gmail.com"
PASSWORD ="Pragat!12345"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("Day 032\quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)
    
        connection =smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="pragatikumari2122@yahoo.com", 
            msg=f"Subject: Have a Nice Day!\n\n{quote}")
