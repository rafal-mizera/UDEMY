from datetime import date

def DaysToGoThisYear(*days):

    for day in days:
        current_year = day.year
        end_of_the_year = date(current_year,12,31)
        days_left = end_of_the_year - day
        print(days_left)

DaysToGoThisYear(date.today(),date(2020,10,10))
