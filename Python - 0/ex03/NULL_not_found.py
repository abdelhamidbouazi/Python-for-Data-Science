def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>");
        return 1;
    if (isinstance(object, float)):
        print("Cheese: nan " + str(type(object)));
        return 1;
    if (object == False):
        print("Fake: False " + str(type(object)));
        return 1;
    if (isinstance(object, int) and object == 0):
        print("Zero: False " + str(type(object)));
        return 1;
    if (object == ''):
        print("Empty: " + str(type(object)));
        return 1;
    if (isinstance(object, str)):
        print("Type not Found");
        return 1;
    return 0;
