class calculator():
    """The Best Calculator: calculate the :
    Dot product, additon and  subtraction
    """
    def __init__(self,  the_list1, the_list2):
        self.the_list1 = the_list1
        self.the_list2 = the_list2

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        dotProduct = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {dotProduct}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        add_vect = [float(v1 + v2) for v1, v2 in zip(V1, V2)]
        print(f"Add Vector is : {add_vect}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        sous_vect = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print(f"Sous Vector is: {sous_vect}")
