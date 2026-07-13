import calendar
from datetime import date

def show_full_year_calendar(year):
    print(f"\nFull Calendar for {year}:\n")
    print(calendar.calendar(year))

def show_month_calendar(year, month):
    print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
    print(calendar.month(year, month))

def is_leap_year(year):
    if calendar.isleap(year):
        print(f"\n{year} is a leap year.")
    else:
        print(f"\n{year} is not a leap year.")

def show_day(year, month, day):
    d = date(year, month, day)
    print(f"\nDate: {d.strftime('%d-%m-%Y')}")
    print(f"Day: {d.strftime('%A')}")

print("Calendar Module")


year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the date (1-31): "))

show_full_year_calendar(year)
show_month_calendar(year, month)
is_leap_year(year)
show_day(year, month, day)
