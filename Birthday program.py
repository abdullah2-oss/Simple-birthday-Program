from datetime import datetime
day = int(input('Enter the day: '))
month = int(input('Enter the month: '))                # Enter your birthday to see if you are an adult or not
year = int(input('Enter the year: '))
birth_date = datetime(year, month, day)
today = datetime.today()
difference = today - birth_date
birth_day = difference.days
birth_year = birth_day // 365
if year <= 18 :
    print(f'You are {birth_year} years old and you are an adult')
else:
    print('You are still not an adult')