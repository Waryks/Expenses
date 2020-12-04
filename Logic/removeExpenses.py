from Domain.getters import getId

def removeAllExpenses(listOfApartments, apartment):
    '''
        Desc: Removes all expenses for a apartment
        In: listOfApartments - list, apartment - int
        Out: -
    '''
    ok = True
    while ok and len(listOfApartments) != 0:
        ok = False
        lenght = len(listOfApartments)
        for index in range(lenght):
            if getId(listOfApartments[index]) == apartment:
                listOfApartments.pop(index)
                ok = True
                break