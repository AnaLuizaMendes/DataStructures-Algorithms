# Exercise elaborated during the course Data Structure & Algorithms
# Inputs: Two dates, valid in the Gregorian Calendar
# Output: How many days between the two dates, considering leap year.
# The code will get each of the next day, and sum it to a variable that will storage the sum of days between dates


# Create a function that will return the number of the days of the month, depending on the year
def days_in_month(year, month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # For leap years feb has 29 days instead of 28
    if leap_year(year):
        months[1] = 29
        # Return the number of the days for month - 1 (because the first index is zero)
        return months[month - 1]
    else:
        return months[month - 1]


# Create a function to check if the year is a leap year or not
# This will modify the days_in_month function, once the quantity of february days will change
def leap_year(year):
    """WARNING! EXCEPTION: Skip leap year if it's a new century (like 1900, 1800, 1700)
     UNLESS is divisible by 400 (like 2000)"""
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    # For any other year (not a new century) just check if divisible by 4
    elif year % 4 == 0:
        return True
    else:
        return False



# Function that get one date and return the next day
def next_day(year, month, day):
    # If it is not the last day in the month (using the daysInMonth function to know if the month has 30/31/28/29 days.
    if day < days_in_month(year, month):
        return year, month, day + 1
    # If it is the last day in the month
    else:
        # If it is December, than increase the year, and set the day and month for 1
        if month == 12:
            return year + 1, 1, 1
        # If it is not December, set the day 1 and increase the month by 1
        else:
            return year, month + 1, 1


# Create a function to be a helper for the dayBetweenDays function to verify if the first date is before the second
def date_is_before(year1, month1, day1, year2, month2, day2):
    # Check for the years
    if year1 < year2:
        return True
    # If same year, check for month and if the months are the same, check days
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2:
            return day1 < day2
    return False


# This is the main function - It will get the two dates as input, and output the number of days between
def days_between_dates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # Starts to generate an error if the dates are not valid (date2 before date1)
    assert not date_is_before(year2, month2, day2, year1, month1, day1)
    # variable to storage the number of days:
    days_between = 0
    # Now we will check if the date1 is before date2
    while date_is_before(year1, month1, day1, year2, month2, day2):
        # Update the values for year, month and day with the nextDay function
        year1, month1, day1 = next_day(year1, month1, day1)
        # And add 1 to each day between the dates, until the first date become the second
        days_between += 1
    return days_between


print(days_between_dates(1900,1,1,1901,1,1))
