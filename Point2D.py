import math

class Point2D:
    nb_points = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point2D.nb_points += 1

    def _get_x(self):
        return self.__x
    
    def _get_y(self):
        return self.__y
    
    def _set_x(self, x):
        self.__x = x

    def _set_x(self, y):
        self.__y = y

    def deplace(self, dx, dy):
        self.__x = self._get_x() + dx
        self.__y = self._get_y() + dy
    
    def distance(self, p):
        dis = 0
        dx = self.__x - p._get_x()
        dy = self.__y - p._get_y()
        square_x = dx * dx
        square_y = dy * dy
        dis = square_x + square_y
        return math.sqrt(dis)
    
    @property
    def rho(self):
        square_x = self._get_x() ** 2
        square_y = self._get_y() ** 2
        addition = square_x + square_y
        return math.sqrt(addition)
    
    @property
    def theta(self):
        return math.degrees(math.atan2(self.__y, self.__x))

    def affiche(self):
        x = self._get_x()
        y = self._get_y()
        print(f"x = {x} y = {y}")

    def __eq__(self, p):
        return p._get_x() == self.__x and p._get_y() == self.__y
        
    @classmethod
    def affiche_nb_point(cls):
        return cls.nb_points
    
    def __doc__(self):
        return "Voici la class Point2D"
    
    def __str__(self):
        return "(" + str(self._get_x()) + ", " + str(self._get_y()) +")"



