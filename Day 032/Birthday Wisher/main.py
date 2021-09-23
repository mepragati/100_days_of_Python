import smtplib

my_email = "testing@gmail.com"
password ="password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="pragati@yahoo.com", msg="Subject:Hello\n\nThis is the testing mail from python.")