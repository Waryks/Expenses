from Logic.define import addExpenses
from Domain.createExpenses import createExpenses
from Logic.monthlyExpenses import monthlyExpenses

def test_monthlyExpenses():
    ex1 = createExpenses(15, 200.0, '15/6/2000', 'sewer')
    ex2 = createExpenses(16, 166.0, '16/4/2000', 'maint')
    ex3 = createExpenses(15, 199.0, '17/12/2000', 'other')
    ex4 = createExpenses(16, 200.0, '15/5/2000', 'sewer')
    ex5 = createExpenses(15, 166.0, '16/3/2000', 'maint')
    ex6 = createExpenses(15, 166.0, '16/3/2000', 'maint')
    list = []
    addExpenses(list, ex1)
    addExpenses(list, ex2)
    addExpenses(list, ex3)
    addExpenses(list, ex4)
    addExpenses(list, ex5)
    addExpenses(list, ex6)
    assert monthlyExpenses(list) == [[15, '6/2000', 200.0], [16, '4/2000', 166.0], [15, '12/2000', 199.0], [16, '5/2000', 200.0], [15, '3/2000', 332.0]]