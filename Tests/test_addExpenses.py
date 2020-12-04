from Logic.define import addExpenses
from Domain.createExpenses import createExpenses
from Domain.getters import getId,getSum,getType
from Logic.addValueToAllExpenses import addValueToAllExpenses

def test_addExpenses():
    expense1 = createExpenses(15, 255.55, "Jun/28/2018", 'sewer')
    expense2 = createExpenses(20, 100, "Jan/18/2019", 'maint')
    list = []
    addExpenses(list,expense1)
    addExpenses(list,expense2)
    assert len(list) == 2
    assert getId(list[0]) == 15
    assert getSum(list[1]) == 100
    assert getType(list[1]) == 'maint'
def test_addValueToAllExpenses():
    ex1 = createExpenses(15, 200.0, '15/June/2000', 'sewer')
    ex2 = createExpenses(15, 166.0, '16/Jan/2000', 'maint')
    ex3 = createExpenses(15, 199.0, '17/March/2000', 'other')
    ex4 = createExpenses(16, 200.0, '15/June/2000', 'sewer')
    ex5 = createExpenses(17, 166.0, '16/jan/2000', 'maint')
    list = []
    addExpenses(list, ex1)
    addExpenses(list, ex2)
    addExpenses(list, ex3)
    addExpenses(list, ex4)
    addExpenses(list, ex5)
    addValueToAllExpenses(list,100, '15/June/2000')
    assert list == ['15,300.0,15/June/2000,sewer', '15,166.0,16/Jan/2000,maint', '15,199.0,17/March/2000,other', '16,300.0,15/June/2000,sewer', '17,166.0,16/jan/2000,maint']