def menu():
    '''
    Desc: Menu
    In: -
    Out: returns option - string
    '''
    print("1. Add expenses")
    print("2. Modify expenses")
    print("3. Delete expenses")
    print("4. Delete all expenses for a apartment")
    print("5. Add a value to a specific date and apartment")
    print("6. Determines the highest expense for each type")
    print("7. Orders the expenses from highest to lowest")
    print("8. Monthly expenses for each apartment")
    print("9. Undo")
    print("10. Redo")
    print("11. Line command")
    print("12. Show list")
    print("Stop - to stop the program")
    op = input("Your option: ")
    return op