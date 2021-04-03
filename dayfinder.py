#This program is to find the last Thursday of the given month. 

# Import Module
import datetime

#Checks the input month has lst day as Thursday and returns TRUE/FALSE
def isLastThursday(date):
    first_day_of_month = datetime.datetime(date.year, date.month, 1)
    next_month_date = first_day_of_month + datetime.timedelta(days=32)
    new_dt = datetime.datetime(next_month_date.year, next_month_date.month, 1)
    Last_day= new_dt - datetime.timedelta(days=1)

    #Checks the last day of the given month is Thursday
    if(Last_day.strftime('%A') == "Thursday"):
        return True
    else:
        return False

def getLastThursday(date):
    # Extract Year From Date
    year = date.year
    # Extract Month From Date
    month = date.month
    Last_day = datetime.date(year + int(month / 12), month % 12 + 1, 1) - datetime.timedelta(days=1)

    #Checks the given month has last day as Thursday
    if (Last_day.strftime('%A') == "Thursday"):
        return Last_day.strftime("%m/%d/%Y %A")
    else:
        return Last_day.strftime("%m/%d/%Y %A")

print("\nLast day of the given month is Thursday ?: ", isLastThursday(datetime.date(2021, 9, 1)))
print("\nLast Day of Month: ", getLastThursday(datetime.date(2021, 9, 24)))

