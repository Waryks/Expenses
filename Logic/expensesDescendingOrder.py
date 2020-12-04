from Domain.getters import getSum

def takeSum(element):
    return getSum(element)
def sortExpenses(listOfApartments):
    '''
        Desc: Sorts expenses in a descending order
        In: listOfApartments - list
        Out: -
    '''
    listOfApartments.sort(key = takeSum,reverse = True)