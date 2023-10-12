import calendar

date = '08 05 2015'

date_arr = date.split(' ')

month = date_arr[0]
day = date_arr[1]
year = date_arr[2]

date_of_the_week = calendar.weekday(int(year), int(month), int(day))
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


print(days[date_of_the_week])