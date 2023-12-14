import datetime

# week_number = datetime.date(2015,6,16).isocalendar()[1]
# print(week_number)

# year_month_date_time = datetime.datetime.now()
# year = year_month_date_time.year
# month = year_month_date_time.month
# day = year_month_date_time.day
# time = year_month_date_time.time()
# week_number = datetime.datetime.today().isocalendar()[1]
# date = datetime.datetime.today()
# print(year_month_date_time)
# print(year)
# print(date.strftime('%B'))
# print(week_number)
# print(date.strftime('%A'))
#
# print(date.strftime('%j'))
# print(date.strftime('%W'))

# date_time_str = 'Jun 28 2018 7:40AM'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
# print('Дата:', date_time_obj.date())
# print('Время:', date_time_obj.time())
# print('Дата и время:', date_time_obj)

# from datetime import date, timedelta
# current_date = date.today().isoformat()
# days_before = (date.today()-timedelta(days=30)).isoformat()
# days_after = (date.today()+timedelta(days=30)).isoformat()
# print("\nCurrent Date: ",current_date)
# print("30 days before current date: ",days_before)
# print("30 days after current date : ",days_after)

# import time
# x=0
# print("\nw3 resource will print five  times, delay for three seconds.")
# while x<5:
#     print("w3resource")
#     time.sleep(3)
#     x=x+1

# import datetime
# from datetime import datetime
# monday1 = 0
# months = range(1,13)
# for year in range(2015, 2017):
#     for month in months:
#         if datetime(year, month, 1).weekday() == 0:
#             monday1 += 1
# print(monday1)

# n = int(input())
# print((30 if n in [4, 6, 9, 11] else 28 if n == 2 else 31))
