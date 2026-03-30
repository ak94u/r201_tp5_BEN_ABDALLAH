class Relationnel:
    nb_Relationnel = 0

    def __init__(self, p, q):
        self.__p = p
        self.__q = q
        Relationnel.nb_Relationnel += 1

    