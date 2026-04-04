from Point2D import Point2D
from Point3D import Point3D
from Rationnel import Rationnel

print("----------------------------------------------------------\n")
print("                             Point2D                      \n")
print("----------------------------------------------------------")

"""Instances de la class Point2D"""
p1 = Point2D(1, 2)
print(p1)

"""Methode d'instances"""
print(p1.__doc__())

print(Point2D.__dict__)

print(hasattr(p1, 'x'))
print(hasattr(p1, 'z'))
print(f"distance = {p1.rho}")
print(f"Theta = {p1.theta}°")

print(Point2D.affiche_nb_point())

print("----------------------------------------------------------\n")
print("                             Point3D                      \n")
print("----------------------------------------------------------")

"""Instances de la class Point3D"""
p2 = Point3D(1, 2, 3)
p3 = Point3D(1, 1, 1)
p4 = Point3D(4, 5, 9)
p5 = Point3D(4, 5, 9)


"""Methode d'instances"""
print(f"distance = {p3.distance(p2)}")
p3.deplace(1, 1, 1)
print(p3)
print(f"rho2 = {p2.rho} et rho3 = {p3.rho}")
print(f"theta2 = {p2.theta}° et theta3 = {p3.theta}°")
print(p2 == p3)
print(f"r_xy2 = {p2.r_xy} et r_xy = {p3.r_xy}")
print(f"phi2 = {p2.phi}° et phi3 = {p3.phi}°")
p2.affiche()
print(Point3D.affiche_nb_point())
print(p4 == p5)


print("----------------------------------------------------------\n")
print("                     class Rationnel                      \n")
print("----------------------------------------------------------")

"""Instances de la class Rationnel"""
r1, r2, r3 = Rationnel(3, 2), Rationnel(2, 3), Rationnel(78, 14)

print(r1.toFloat())
print(r2.toFloat())
print(r1)
print(r2)

r3new = r3.simplifier()
print(r3)
print(f"simplifiacation de r3: {r3} devient {r3new}")

print(f"{r3} = {r3new} = {r3 == r3new}")
print(f"{r1} + {r2} = {r1 + r2}")
print(f"{r1} - {r2} = {r1 - r2}")
print(f"{r1} x {r2} = {r1 * r2}")
print(f"({r1}) / ({r2}) = {r1 / r2}")
print(f"{r1} > {r2} = {r1 > r2}")
print(f"{r1} < {r2} = {r1 < r2}")
print(f"{r1} >= {r2} = {r1 >= r2}")
print(f"{r1} <= {r2} = {r1 <= r2}\n")
print(f"{r3} >= {r3new} = {r3 >= r3new}")
print(f"{r3} <= {r3new} = {r3 >= r3new}")

print(f"Le nombre de nombres rationnel construit : {Rationnel.affiche_nb_point()}\n")
print("Notice: chaque fois que vous faites un clacule un nouveau nombres rationnel se contruit")


