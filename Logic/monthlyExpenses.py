from Domain.getters import getId,getSum,getDate,getDay,getMonth,getYear

def monthlyExpenses(expensesList):
    '''
    Desc: Function calculates the monthly expenses of every apartment
    In: spendingsList: - list - the list that contains the spendings
    Out: returns subList - list of lists - a big list that contains small lists in the form of [apartment number, month, total]
    '''
    list = []
    for index_i in range(len(expensesList)):
        total = 0
        cAp = getId(expensesList[index_i])
        cMth = getMonth(getDate(expensesList[index_i]))
        cYear = getYear(getDate(expensesList[index_i]))
        for index_j in range(index_i + 1, len(expensesList)):
            if getId(expensesList[index_j]) == cAp and getMonth(getDate(expensesList[index_j])) == cMth and getYear(getDate(expensesList[index_j])) == cYear:
                total += getSum(expensesList[index_j])
        total += getSum(expensesList[index_i])
        nowList = [cAp, str(cMth) + "/" + str(cYear), total]
        list.append(nowList)
    list = removeDuplicates(list)
    return list

def removeDuplicates(lists):
    '''
    Desc: Function removes the duplicates from a list
    In: lists: - list of list
    Out - lists - the new list of list without dups
    '''
    for index_i in range(len(lists)-1):
        first = lists[index_i][0]
        second = lists[index_i][1]
        for index_j in range(index_i+1,len(lists)):
            verif = False
            if lists[index_j][0] == first and lists[index_j][1] == second:
                lists.pop(index_j)
                verif = True
            if verif == True:
                index_j -=1
    return lists

