# import calendar
# # sep=calendar.TextCalendar(calendar.SUNDAY)
# # sep.prmonth(2017, 9)

# # leaps=calendar.leapdays(1900, 2018)
# # print(leaps)

# # print("########## Leap Year Calendar ##########\n")
# # y1=int(input("Enter the first year: "))
# # y2=int(input("Enter the second year: "))
# # leaps=calendar.leapdays(y1, y2)
# # print("Number of leap years between", y1, "and", y2, "is:", leaps)

# year=int(input("Enter the year to display: "))
# print(calendar.prcal(2018))

# print(calendar.leapdays(2001, 2018))

# import calendar
# cal=calendar.TextCalendar(calendar.MONDAY)
# for i in cal.itermonthdates(2019, 1):
#     print(i)

# import calendar
# for name in calendar.month_name:
#     print(name)

# import calendar
# for name in calendar.day_name:
#     print(name)

import calendar
cal=open("./cal.html", "w")
c=calendar.HTMLCalendar(calendar.MONDAY)
cal.write(c.formatmonth(2019, 1))
cal.close()
