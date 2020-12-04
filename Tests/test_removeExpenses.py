from Logic.define import addExpenses
from Domain.createExpenses import createExpenses
from Logic.removeExpenses import removeAllExpenses

def test_removeExpenses():
    expense1 = createExpenses(15, 255.55, "Jun/28/2018", 'sewer')
    expense2 = createExpenses(20, 100, "Jan/18/2019", 'maint')
    list = []
    addExpenses(list, expense1)
    addExpenses(list, expense2)
    removeAllExpenses(list,20)
    assert len(list) == 1