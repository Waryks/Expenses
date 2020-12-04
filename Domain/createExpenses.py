def createExpenses(apartment, sum, date, type):
    '''
        Desc: Creates expense for a apartment
        In: apartment - int, sum - float, date - string, type - string
        Out: returns rent - a list that contains the specs for the rent
    '''
    rent = ','.join([str(apartment), str(sum), date, type])
    return rent