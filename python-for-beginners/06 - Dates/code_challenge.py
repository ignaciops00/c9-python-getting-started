# print today's date
# print yesterday's date
# ask a user to enter a date
# print the date one week from the date entered
from datetime import datetime, timedelta

currentdate = datetime.now()

print(str(currentdate - timedelta(days=1)))
print(str(currentdate + timedelta(weeks=1)))

print(f"{currentdate:%d/%m/%Y}")
print('{:%d - %m - %Y}'.format(currentdate))