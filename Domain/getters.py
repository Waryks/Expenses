def getId(apartment):
    '''
        Desc: Gets the number of the apartment
        In: apartment - str
        Out: returns the number of the apartment int
    '''
    command = apartment.split(",")
    return int(command[0])

def getSum(apartment):
    '''
        Desc: Gets the sum that the apartment owner has to pay
        In: apartment - str
        Out: returns the sum float
    '''
    command = apartment.split(",")
    return float(command[1])

def getDate(apartment):
    '''
        Desc: Gets the date when the expense was made
        In: apartment - str
        Out: returns the date - str
    '''
    command = apartment.split(",")
    return command[2]

def getType(apartment):
    '''
        Desc: Gets the type of expense
        In: apartment - str
        Out: returns the type - str
    '''
    command = apartment.split(",")
    return command[3]

def getMonth(date):
    '''
        Desc: Function returns the month of a given date
        In: date - string
        Out: returns the month of the given date
    '''
    dateList = date.split("/")
    return dateList[1]


def getYear(date):
    '''
        Desc: Function returns the year of a given date
        In: date - string - the given date
        Out: returns the year of the given date
    '''
    dateList = date.split("/")
    return dateList[2]

def getDay(date):
    '''
        Desc: Function returns the day of a given date
        In: date - string - the given date
        Out: returns the year of the given date
    '''
    dateList = date.split("/")
    return dateList[0]