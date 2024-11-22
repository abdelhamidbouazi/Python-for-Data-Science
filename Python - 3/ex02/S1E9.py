from abc import ABC, abstractmethod


class Character(ABC):
    """Character abstract class"""
    first_name = ''
    is_alive = True

    @abstractmethod
    def __init__(self, first_name, *args):
        """The contructor of the class Character"""
        self.first_name = first_name
        if len(args) > 0:
            self.is_alive = args[0]

    def die(self):
        """The die method docstring in superclass"""
        self.is_alive = False


class Stark(Character):
    """The derived class Stark"""
    def __init__(self,  first_name, *args):
        """Contructor of the class Stark"""
        self.first_name = first_name
        self.is_alive = True
        if len(args) > 0:
            self.is_alive = args[0]
