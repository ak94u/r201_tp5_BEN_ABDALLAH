import Point2D
import Point3D

p1 = Point2D(1, 2)
print(p1)

print(p1.__doc__())

print(Point2D.__dict__)

print(hasattr(p1, 'x'))
print(hasattr(p1, 'z'))
print(p1.rho)
print(p1.theta)

print(Point2D.affiche_nb_point())