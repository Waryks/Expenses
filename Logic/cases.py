from Logic.monthlyExpenses import getMonth, getYear, getDay
import datetime

eps = 0.000001

def isInt(value):
    '''
    Desc: Is it int?
    In: value - param
    Out: True/False
    '''
    try:
        int(value)
        return True
    except ValueError:
        return False # it was a string, not an int.


def isFloat(value):
    '''
    Is it float?
    In: value - param
    Out True/False
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False # it was a string, not a float.


def isDate(date):
    '''
    Desc: Me: Is this a date??? *gets friendzoned*
    In: date: - string
    Out: True/False
    '''
    if isInt(getDay(date)) and isInt(getMonth(date)) and isInt(getYear(date)):
        if int(getDay(date)) < 1 or int(getMonth(date)) < 1 or int(getYear(date)) < 1:
            return False
        if int(getMonth(date)) > 12:
            return False
        if int(getMonth(date)) == 2 and int(getDay(date)) > 29:
            return False
        if int(getMonth(date)) < 8 and int(getMonth(date))%2 == 1 and int(getDay(date)) > 31:
            return False
        if int(getMonth(date)) < 8 and int(getMonth(date))%2 == 0 and int(getDay(date)) > 30:
            return False
        if int(getMonth(date)) > 8 and int(getMonth(date))%2 == 1 and int(getDay(date)) > 30:
            return False
        if int(getMonth(date)) > 8 and int(getMonth(date))%2 == 0 and int(getDay(date)) > 31:
            return False
        if int(getYear(date)) > datetime.datetime.now().year:
            return False
        return True
    else:
        return False


def isApartment(apartNumber):
    '''
    Desc: Is it a APARTMENT???
    In: date: - string
    Out: True/False
    '''
    if isInt(apartNumber):
        if int(apartNumber) < 1 or int(apartNumber) > 99999:
            return False
        return True
    return False

def isPozFloat(value):
    if isFloat(value):
        if float(value) <= 0 + eps:
            return False
        return True
    return False

def dipCopy(listToCopy):
    list = []
    for index in range(len(listToCopy)):
        list.append(listToCopy[index])
    return list