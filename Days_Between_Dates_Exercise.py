# Exercise elaborated during the course Data Structure & Algorithms
# Inputs: Two dates, valid in the Gregorian Calendar
# Output: How many days between the two dates, considering leap year.
# The code will get each of the next day, and sum it to a variable that will storage the sum of days between dates

# Function that get one date and return the next day
def nextDay(year, month, day):
    # If it is not the last day in the month
    if day < 30:
        return year, month, day + 1
    # If it is the last day in the month
    else:
        # If it is December, than increase the year, and set the day and month for 1
        if month == 12:
            return year + 1, 1, 1
        # If it is not December, set the day 1 and increase the month by 1
        else:
            return year, month + 1, 1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # Starts to generate an error if the dates are not valid (date2 before date1)
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    # variable to storage the number of days:
    days_between = 0
    # Now we will check if the date1 is before date2
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        # Update the values for year, month and day with the nextDay function
        year1, month1, day1 = nextDay(year1, month1, day1)
        # And add 1 to each day between the dates, until the first date become the second
        days_between += 1
    return days_between


# Create a function to be a helper for the dayBetweenDays function to verify if the first date is before the second
def dateIsBefore(year1, month1, day1, year2, month2, day2):
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




print(daysBetweenDates(2012, 9, 30, 2012, 10, 30))
