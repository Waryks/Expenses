def createObject(apartment, sum , date, type):
    """
    Desc: Creates an object
    In: apartmen = int, sum float, date str, type str
    Out: list
    """
    return '{}, {}, {}, {}'.format(apartment, sum , date, type)
def setPosition(object, position: int, value):
    """
        Desc: used by the setters, in order to modify the proprieties of an object
        In: -object: list
            -position: int
            -value: int or string
        Out: a modified object
    """
    objectProp = object.split(sep=", ")
    objectProp[position] = value
    return createObject(
        objectProp[0],
        objectProp[1],
        objectProp[2],
        objectProp[3]
    )

def setApartment_List(object, newApartment):
    return setPosition(object, 0, newApartment)
def setSum_List(object, newSum):
    return setPosition(object, 1, newSum)
def setDate_List(object, newDate):
    return setPosition(object, 2, newDate)
def setType_List(object, newType):
    return setPosition(object, 3, newType)
