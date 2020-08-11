from math import pi, pow
 
def rectangle(a, b):
    return round(a * b, 2)
 
def triangle(a, h):
    return round(0.5 * a * h, 2)
 
def circle(r):
    return round(pi * pow(r, 2), 2) 