from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, *args):
        """Constructor for Baratheon family."""
        self.first_name = first_name
        self.is_alive = True
        self.family_name = self.__class__.__name__
        if len(args) > 0:
            self.is_alive = args[0]
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """Overriding the __str__ behavior."""
        return (
            f"Vector: ('{self.__class__.__name__}', "
            f"'{self.eyes}', '{self.hairs}')"
        )

    def __repr__(self):
        """Overriding the __repr__ behavior."""
        return (
            f"Vector: ('{self.__class__.__name__}', "
            f"'{self.eyes}', '{self.hairs}')"
        )


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, *args):
        """Constructor for Lannister family."""
        self.first_name = first_name
        self.is_alive = True
        self.family_name = self.__class__.__name__
        if len(args) > 0:
            self.is_alive = args[0]
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """Overriding the __str__ behavior."""
        return (
            f"Vector: ('{self.__class__.__name__}', "
            f"'{self.eyes}', '{self.hairs}')"
        )

    def __repr__(self):
        """Overriding the __repr__ behavior."""
        return (
            f"Vector: ('{self.__class__.__name__}', "
            f"'{self.eyes}', '{self.hairs}')"
        )

    @classmethod
    def create_lannister(cls, first_name, *args):
        """Decorator class method to get instance of the class"""
        lannister = cls(first_name, *args)
        lannister.first_name = first_name
        lannister.is_alive = True
        if len(args) > 0:
            lannister.is_alive = args[0]
        return lannister
