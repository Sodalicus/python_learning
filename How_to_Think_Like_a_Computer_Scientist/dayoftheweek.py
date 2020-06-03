#!/usr/bin/env python

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def day(number):
    if number in range(6):
        return days[number]
    else:
        info = 'Wrong day number'
        return info


def day_of_return(st_day, lenght):
    return day(((st_day+lenght)%7))


st_day = 1
holiday = 7
print("Starting day is", day(st_day))
print("Holiday lenght is",holiday,"days.")
print("Returning day is",day_of_return(st_day, holiday))
