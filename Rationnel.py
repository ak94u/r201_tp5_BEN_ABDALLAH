class Rationnel:
    nb_Relationnel = 0

    def __init__(self, p, q):
        self.__p = p
        self.__q = q
        Rationnel.nb_Relationnel += 1

    def __str__(self):
        if self._get_Denum() == 0 :
            return False
        return str(self._get_Num()) + "/" + str(self._get_Denum())
    
    def _get_Num(self):
        return self.__p
    
    def _set_Num(self, p):
        self.__p = p
    
    def _get_Denum(self):
        return self.__q
    
    def _set_Q(self, q):
        self.__q = q

    def toFloat(self):
        if self.__q == 0:
            print("(P | Q) n'est pas défini en 0")
            return False
        else: 
            return self._get_Num() / self._get_Denum()
        
    @staticmethod
    def PGCD(a, b):
        a, b = abs(a), abs(b)
        while b != 0:
            a, b = b, a % b
        return a


    def simplifier(self):
        p = self.PGCD(self.__p, self._q)
        
        a = self.__p // p
        b = self.__q // p


    def __eq__(self, r):
        return self.__p == r._get_Num() and self.__q == r._get_Denum()
    
    def __add__(self, r):
        p_new = self.__p * r._get_Denum() + r._get_Num() * self.__q
        q_new = self.__q * r._get_Denum()

        return Rationnel(p_new, q_new)
    
    def __mul__(self, r):
        return self.__p * r._get_Num() + self.__q * r._get_Denum()
    
    def __sub__(self, r):
        p_new = self.__p * r._get_Denum() - r._get_Num() * self.__q
        q_new = self.__q * r._get_Denum()

        return Rationnel(p_new, q_new)
    
    def __truediv__(self, r):
        p_new = self.__p * r.get_Denum()
        q_new = self.__q * r.get_Num()

        return Rationnel(p_new, q_new)
    
    def __ne__(self, r):
       return self.__p != r._get_Num() and self.__q != r._get_Denum()
    
    def __gt__(self, r):
        return self.__p * r.get_Denum() > r.get_Num() * self.__q
    
    def __ge__(self, r):
        return self.__p * r.get_Denum() >= r.get_Num() * self.__q
    
    def __lt__(self, r):
        return self.__p * r.get_Denum() < r.get_Num() * self.__q
    
    def __le__(self, r):
        return self.__p * r.get_Denum() <= r.get_Num() * self.__q
        