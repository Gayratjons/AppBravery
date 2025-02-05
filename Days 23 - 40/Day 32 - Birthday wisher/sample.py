import smtplib
my_email = "umarbek777@gmail.com"
password = "Umarbek77701"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="appbrewerytesting@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
