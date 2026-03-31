class Relationnel:
    nb_Relationnel = 0

    def __init__(self, p, q):
        self.__p = p
        self.__q = q
        Relationnel.nb_Relationnel += 1

    def _get_P(self):
        return self.__p
    
    def _set_P(self, p):
        self.__p = p
    
    def _get_Q(self):
        return self.__q
    
    def _set_Q(self, q):
        self.__q = q

    def __str__(self):
        if self._get_Q() == 0 :
            return -1
        
        return str(self._get_P()) + "/" + str(self._get_Q())
    
    