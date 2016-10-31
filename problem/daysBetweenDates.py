# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.



def leap_year(x):
    if x % 4 != 0:
        return False
    elif x % 100 != 0:
        return True
    elif x % 400 != 0:
        return False
    else:
        return True


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if leap_year(year):
        daysOfMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < daysOfMonths[month - 1]:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()





# # By Websten from forums
# #
# # Given your birthday and the current date, calculate your age in days.
# # Account for leap days.
# #
# # Assume that the birthday and current date are correct dates (and no
# # time travel).
# #
#
# def leap_year(x):
#     if x % 4 != 0:
#         nleap = 0
#     elif x % 100 != 0:
#         nleap = 1
#     elif x % 400 != 0:
#         nleap = 0
#     else:
#         nleap = 1
#     return nleap
#
#
# daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     ##
#     # Your code here.
#     ##
#     n = 0
#     nleapyear = 0
#     year = year1
#
#     while year + 1 < year2:
#         nleapyear = nleapyear + leap_year(year + 1)
#         year = year + 1
#     nyear = (year2 - year1 - 1) * 365 + nleapyear
#
#     if year1 == year2:
#         nyear = -365 - leap_year(year1)
#
#     nmonth = 0
#     month = month1
#     while month + 1 <= 12:
#         nmonth = nmonth + daysOfMonths[month]  # start from 0
#         month = month + 1
#     if month1 + 1 <= 2:
#         nmonth = nmonth + leap_year(year1)
#
#     month = 1
#     while month <= month2 - 1:
#         nmonth = nmonth + daysOfMonths[month - 1]
#         month = month + 1
#     if month2 - 1 >= 2:
#         nmonth = nmonth + leap_year(year2)
#
#     nday = 0
#     nday = daysOfMonths[month1 - 1] - day1 + day2
#     if month1 == 2:
#         nday = nday + leap_year(year1)
#
#     n = nyear + nmonth + nday
#     return n
#
#
# # Test routine
#
# def test():
#     test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
#                   ((2012, 1, 1, 2012, 3, 1), 60),
#                   ((2011, 6, 30, 2012, 6, 30), 366),
#                   ((2011, 1, 1, 2012, 8, 8), 585),
#                   ((1900, 1, 1, 1999, 12, 31), 36523)]
#     for (args, answer) in test_cases:
#         result = daysBetweenDates(*args)
#         if result != answer:
#             print("Test with data:", args, "failed")
#         else:
#             print("Test case passed!")
#
#
# test()
#
#
