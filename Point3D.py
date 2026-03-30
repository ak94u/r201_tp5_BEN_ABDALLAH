from Point2D import Point2D
import math

class Point3D(Point2D):
    nb_points = 0

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z
        Point3D.nb_points += 1
    
    def _get_z(self):
        return self.__z
    
    def _set_z(self, z):
        self.__z = z

    def deplace(self, dx, dy, dz):
        super().deplace(dx, dy)
        self.__z = self._get_z() + dz
       
    def distance(self, p):
        d3D = 0
        dz = self.__z - p._get_z()
        square_z = dz ** 2
        d2D = super().distance(p)
        d3D = d2D**2 + square_z
        return math.sqrt(d3D)
    
    @property
    def rho(self):
       """ Distance à l'origine (rayon sphérique) """
       rho2D = super().rho()
       square_z = self._get_z() ** 2
       return math.sqrt(rho2D ** 2 + square_z)
    
    @property 
    def r_xy(self): 
        """ Projection dans le plan XY (rayon cylindrique) """
        return math.sqrt(self.__x ** 2 + self.__y **2)
    
    def theta(self): 
        """Angle azimutal dans le plan XY -- entre -180° et 180°"""
        return math.degrees(math.atan2(self.__y, self.x))
    
    def phi(self):
        """Angle polaire depuis l'axe Z (colatitude) - entre 0° et 180°"""
        if self.rho == 0:
            return 0.0
        return math.degrees(math.acos(self.__z / self.rho))
    
    def affiche(self):
        x = self.__x
        y = self.__y
        z = self.__z
        print(f"x = {x}, y = {y}, z = {z}")

    @classmethod
    def affiche_nb_point(cls):
        return cls.nb_points
    
    def __eq__(self, p):
        return super().__eq__(p) and p._get_z() == self.__z
    
    def __str__(self):
        return "(" + str(self._get_x()) + ", " + str(self._get_y()) + str(self._get_z()) + ")"