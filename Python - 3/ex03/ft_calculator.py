class calculator():
    """The operators + - * / overloads"""
    def __init__(self,  the_list):
        self.the_list = the_list

    def __add__(self, object) -> None:
        self.the_list = [ob + object for ob in self.the_list]
        print(self.the_list)

    def __mul__(self, object) -> None:
        self.the_list = [ob * object for ob in self.the_list]
        print(self.the_list)

    def __sub__(self, object) -> None:
        self.the_list = [ob - object for ob in self.the_list]
        print(self.the_list)

    def __truediv__(self, object) -> None:
        if object != 0:
            self.the_list = [ob / object for ob in self.the_list]
            print(self.the_list)
        else:
            print("Error: Cannot divide by Zero")
