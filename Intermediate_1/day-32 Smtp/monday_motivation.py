import smtplib
import random
import datetime as dt

# Your credentials (ensure these are correct and secure)
email_address = "anirbansarkar.slg18@gmail.com"  # Replace with your email address
my_password = "tkrf jtuw rmei fryy"  # Replace with your password
to_address = 'anirbansarkar9967@gmail.com'  # Replace with recipient's email address

now = dt.datetime.now()
weekday = now.weekday()
subject = 'Monday Motivation'

if weekday == 0: 
    try:
        
        with open(r'day-32 Smtp\quotes.txt') as quote_file:
            allQt = quote_file.readlines()
        
        if allQt:  # Check if there are any lines in the file
            quote = random.choice(allQt).strip()  # .strip() to remove any extra newlines
        else:
            quote = "No quotes available."

        print(quote)

        # Sending email
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=email_address, password=my_password)
            connection.sendmail(
                from_addr=email_address,
                to_addrs=to_address,
                msg=f"Subject: {subject}\n\n{quote}"
            )
        print("Email sent successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print("Today is not Monday. No email sent.")
