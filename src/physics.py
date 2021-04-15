import math
import sys

def Velocity(energy, mass):
    c = 2*energy
    b = c/mass
    a = b**0.5
    return a

def Vectorx(velocity, angle):
    x = -math.cos(math.degrees(angle)) * velocity
    return x

def Vectory(velocity, angle):
    y = math.sin(math.degrees(angle)) * velocity
    return y

def Gravity(height):
    G = 6.674e-11
    EM = 5.9724e24
    ER = 6.378137e6
    g = G * EM/((ER+height)**2)
    return g

def Distance(velocity, angle):
    v = [Vectorx(velocity, angle), Vectory(velocity, angle)]
    meters = ((velocity**2) * math.sin(math.degrees(2*angle))/9.81)
    return meters

print(Distance(Velocity(
        int(input()),
        int(input())
    ),
    int(input())
))
