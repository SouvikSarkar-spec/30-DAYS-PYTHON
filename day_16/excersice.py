from datetime import *
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute} and timestamp is {timestamp}")
tday=now.strftime("%m/%d/%Y, %H:%M:%S")
print(tday)
str="5 December, 2019"
formatted_time=datetime.strptime(str,"%d %B, %Y")
print(formatted_time)
now=datetime.today()
new_year=datetime(2027,1,1)
print(f'the difference is {new_year-now}')
epoch=datetime(1970,1,1)
print(now-epoch)