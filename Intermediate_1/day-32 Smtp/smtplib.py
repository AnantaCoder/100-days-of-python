import smtplib

email_address = "anirbansarkar8@gmail.com"
my_password = ""
to_address = 'anneetai19@gmail.com'
subject = "Happy Birthday"
message_body = 'I am Anirban Sarkar and happy birthday to you ji!'

message = f"Subject: {subject}\n\n{message_body}"

with smtplib.SMTP('smtp.gmail.com', 587) as connection: 
    connection.starttls()
    connection.login(user=email_address, password=my_password)
    connection.sendmail(
        from_addr=email_address,
        to_addrs=to_address,
        msg=message
    )
