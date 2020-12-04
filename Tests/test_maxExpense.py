from Logic.define import addExpenses
from Domain.createExpenses import createExpenses
from Logic.maxExpense import maxExpenses

def test_maxExpenses():
    ex1 = createExpenses(15, 200.0, '15/June/2000', 'sewer')
    ex2 = createExpenses(15, 166.0, '16/Jan/2000', 'maint')
    ex3 = createExpenses(15, 199.0, '17/March/2000', 'other')
    ex4 = createExpenses(16, 200.0, '15/june/2000', 'sewer')
    ex5 = createExpenses(17, 166.0, '16/jan/2000', 'maint')
    list = []
    addExpenses(list, ex1)
    addExpenses(list, ex2)
    addExpenses(list, ex3)
    addExpenses(list, ex4)
    addExpenses(list, ex5)
    assert maxExpenses(list) == [[200.0, 'sewer'], [166.0, 'maintenance'], [199.0, 'others']]