import math
import sys

def Velocity(energy, mass):
    c = 2*energy
    b = c/mass
    a = b**0.5
    return a

def distance(energy, mass, angle):
    v = Velocity(energy, mass)
    print("Velocidad inicial: ", v)
    meters = 0
    seconds = 0
    g = 9.8
    vx = math.cos(angle) * v
    print("Velocidad en x: ", vx)
    vy = -math.sin(angle) * v
    print("Velocidad en y: ", vy)
    time = (2 * vy)/g
    meters = time * vx
    #height = 2 + vy
    #while height >= 0:
    #    height -= g * 10e-4
    #    seconds += 10e-4 * 1
    #    print(seconds)
    #meters = seconds * vx
    return meters

def energy(mass, velocity):
    v = velocity
    m = mass
    J = 1/2 * (m*(v**2))
    return J

def mass(energy, velocity):
    J = energy
    v = velocity
    mass = (2*J)/v
    return mass

print("Distancia: ", distance(
    int(input("Energy: \n")),
    int(input("Mass: \n")),
    int(input("Angle: \n"))
    ))
