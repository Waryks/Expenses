from Domain.getters import getType,getSum

def maxExpenses(listOfApartments):
    '''
            Desc: Shows the max expense for each type of expense
            In: listOfApartments - list
            Out: listMax - list of expenses
    '''
    maxSewer = 0
    maxMaintenance = 0
    maxOthers = 0
    for apartment in listOfApartments:
        if getType(apartment) in "sewer" and getSum(apartment) > float(maxSewer) :
            maxSewer = getSum(apartment)
        if getType(apartment) in "maintenance" and getSum(apartment) > float(maxMaintenance) :
            maxMaintenance = getSum(apartment)
        if getType(apartment) in "others" and getSum(apartment) > float(maxOthers) :
            maxOthers = getSum(apartment)
    listMax = []
    listMax.append([float(maxSewer), "sewer"])
    listMax.append([float(maxMaintenance), "maintenance"])
    listMax.append([float(maxOthers), "others"])
    return listMax