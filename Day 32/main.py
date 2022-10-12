import smtplib
import datetime as dt

my_email = "automatedemailclientproject@gmail.com"
password = "PythonTest32;"




now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 1:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="violahandal@gmail.com",
                            msg="Subject:Automated e-mail sender project TEST\n\nHELLO CRAZY FRIEND!! I MADE MY PROGRAM CHECK IF IT IS TUESDAY, AND IT IS SO IT SENDS EMAIL AHHHHH!!!!")
