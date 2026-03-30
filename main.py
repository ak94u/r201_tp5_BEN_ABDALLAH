"""from Point2D import Point2D"""
from Point3D import Point3D

"""p1 = Point2D(1, 2)
print(p1)

print(p1.__doc__())

print(Point2D.__dict__)

print(hasattr(p1, 'x'))
print(hasattr(p1, 'z'))
print(p1.rho)
print(p1.theta)

print(Point2D.affiche_nb_point())"""

p2 = Point3D(1, 2, 3)
p3 = Point3D(1, 1, 1)
p4 = Point3D(4, 5, 9)
p5 = Point3D(4, 5, 9)


print(f"distance = {p3.distance(p2)}")
p3.deplace(1, 1, 1)
print(p3)
print(f"rho2 = {p2.rho} et rho3 = {p3.rho}")
print(f"theta2 = {p2.theta} et theta3 = {p3.theta}")
print(p2 == p3)
print(f"r_xy2 = {p2.r_xy} et r_xy = {p3.r_xy}")
print(f"phi2 = {p2.phi} et phi3 = {p3.phi}")
p2.affiche()
print(Point3D.affiche_nb_point())
print(p4 == p5)

