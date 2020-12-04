from Logic.define import addExpenses,modifyExpenses
from Domain.createExpenses import createExpenses
from Domain.getters import getSum

def test_modifyExpenses():
    expense1 = createExpenses(15, 255.55, "Jun/28/2018", 'sewer')
    expense2 = createExpenses(20, 100, "Jan/18/2019", 'maint')
    list = []
    addExpenses(list, expense1)
    addExpenses(list, expense2)
    modifyExpenses(list,15, 'sewer', 'Jun/18/2019', 200)
    assert getSum(list[0]) == 200

