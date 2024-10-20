def all_thing_is_obj(object: any) -> int:
    if (isinstance(object, int)):
        return 42;
    if (isinstance(object, str)):
        print(object + " is in the kitchen : " + str(type(object)));
        return 42;
    else:
        print(type(object).__qualname__ .capitalize() + " : " + str(type(object)))
        return 42;

