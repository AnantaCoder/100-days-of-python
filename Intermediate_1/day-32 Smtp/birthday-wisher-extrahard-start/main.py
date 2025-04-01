import datetime as dt
import smtplib
import random 
import math 
import pandas as pd 

MY_EMAIL = "anirbansarkar.slg18@gmail.com"
MY_PASSWORD = "itot thnc ullc uwqf"
# 1. Read the CSV file
dataset = pd.read_csv('day-32 Smtp//birthday-wisher-extrahard-start//birthdays.csv')

# 2. Extract the year, month, and day values from the first row (assuming you meant column 0, which is the first column)
name = dataset.iloc[0, 0]  
year = dataset.iloc[0, 2]  
month = dataset.iloc[0, 3] 
day = dataset.iloc[0, 4]  
email = dataset.iloc[0,1]


# 2. Check if today matches a birthday in the birthdays.csv
today= dt.datetime.now()
file1 = 'day-32 Smtp//birthday-wisher-extrahard-start//letter_templates//letter_1.txt'
file2 = 'day-32 Smtp//birthday-wisher-extrahard-start//letter_templates//letter_2.txt'
file3 = 'day-32 Smtp//birthday-wisher-extrahard-start//letter_templates//letter_3.txt'
txt_files = [file1,file2,file3]
selected_file= random.choice(txt_files)
if today.month == month and today.day== day :
    try:
        with open(selected_file , 'r') as file:
            content= file.read()
        # 3. Replace the [NAME] placeholder with the actual birthday person's name
        content = content.replace('[NAME]', name)
        
        
        with smtplib.SMTP('smtp.gmail.com',port=587, timeout=60) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg = f'Subject : Happy Birthday!\n\n{content}' 
            )
        
        print('Email Sent')
        
    except Exception as e:
        print(f"An error occurred: {e}")
else:
     print("Today is not a birthday.") 


