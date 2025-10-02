import calendar
import datetime

WEEKDAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
OPTIONS = {
    'first': 0,
    'second': 1,
    'third': 2,
    'fourth':3,
    'fifth':4,
    'last':-1,
    'teenth': 10
}

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self,message):
        self.message = message


def meetup(year, month, week, day_of_week):
    
    month_calendar = calendar.monthcalendar(year,month)
    weekdays = []
    for i in range(0,7):
        result = []
        for j in range(0,len(month_calendar)):
            result.append(month_calendar[j][i])
        weekdays.append(result)


    weekdays = [[day for day in weekday if day != 0] for weekday in weekdays]
    reference = dict(zip(WEEKDAYS,weekdays))[day_of_week]

    if week not in OPTIONS.keys():
        raise ValueError('Option unknown.')
    
    option = OPTIONS[week]

    try:
        if option <= 4:
            return datetime.date(year,month,reference[option])
        else:
            reference = [day for day in reference if 13 <= day <= 19]
            return datetime.date(year,month,reference[0])


    except IndexError:
        raise MeetupDayException("That day does not exist.")        

