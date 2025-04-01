import datetime as dt

now = dt.datetime.now()

# Extracting specific components
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
day_of_week = now.weekday()

print(f"Year: {year}, Month: {month}, Day: {day}")
print(f"Hour: {hour}, Minute: {minute}, Second: {second}")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"Today is: {days[day_of_week]}")

