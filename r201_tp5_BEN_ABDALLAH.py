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
        
        return(dx, dy)
    
    def distance(self, p):
        dx = self.__x - p._get_x()
        dy = self.__y - p._get_y()
        square_x = dx * dx
        square_y = dy * dy
        return math.sqrt(square_x + square_y)
    
    @property
    def rho(self):
        square_x = self._get_x() ** 2
        square_y = self._get_y() ** 2
        addition = square_x + square_y
        return math.sqrt(addition)
    
    @property
    def theta(self):
        angle = 0
        if self.__x == 0 :
            return math.degrees(math.atan2(self.__y, self.__x))
        else:
            x = math.acos(self.__x/ self.rho)
            y = math.asin(self.__y/ self.rho)
            angle = y/x
            return math.degrees(angle)
        

    def affiche(self):
        x = self._get_x
        y = self._get_y
        print(f"x = {x} y = {y}")
        
    @classmethod
    def affiche_nb_point(cls):
        return cls.nb_points
    
    def __doc__(self):
        return "Voici la class Point2D"
    
    def __str__(self):
        return "(" + str(self._get_x()) + ", " + str(self._get_y()) +")"

p1 = Point2D(1, 2)
print(p1)

print(p1.__doc__())

print(Point2D.__dict__)

print(hasattr(p1, 'x'))
print(hasattr(p1, 'z'))
print(p1.rho)
print(p1.theta)

print(Point2D.affiche_nb_point())

