import math
from collections import namedtuple

Body = namedtuple("Body", "name radius_km color au period_days eccentricity phase_deg parent")

# Colors (RGB 0..1 for VPython)
SUN    = (1.0, 0.84, 0.47)
MERC   = (0.66, 0.66, 0.66)
VENUS  = (0.85, 0.70, 0.36)
EARTH  = (0.39, 0.58, 0.93)
MOON   = (0.85, 0.85, 0.85)
MARS   = (0.74, 0.15, 0.20)
JUP    = (0.85, 0.65, 0.46)
SAT    = (0.82, 0.71, 0.55)
URAN   = (0.69, 0.93, 0.93)
NEPT   = (0.28, 0.46, 1.0)
PLUTO  = (0.78, 0.78, 0.66)

BODIES = [
    Body("Sun",     695700, SUN,   0.0,     1.0,   0.0,   0.0, None),
    Body("Mercury",   2440, MERC,  0.39,   87.97,  0.205, 40.0, "Sun"),
    Body("Venus",     6052, VENUS, 0.723, 224.70,  0.007,120.0, "Sun"),
    Body("Earth",     6371, EARTH, 1.00,  365.256, 0.017, 10.0, "Sun"),
    Body("Moon",      1737, MOON,  0.00257, 27.32, 0.055,  0.0, "Earth"),
    Body("Mars",      3390, MARS,  1.524, 686.98,  0.093,200.0, "Sun"),
    Body("Jupiter",  69911, JUP,   5.203, 4332.59, 0.049,  0.0, "Sun"),
    Body("Saturn",   58232, SAT,   9.537,10759.22, 0.056,  0.0, "Sun"),
    Body("Uranus",   25362, URAN, 19.191,30685.4,  0.047,  0.0, "Sun"),
    Body("Neptune",  24622, NEPT, 30.068,60190.0,  0.009,  0.0, "Sun"),
    Body("Pluto",     1188, PLUTO, 39.48, 90560.0, 0.249,  0.0, "Sun"),
]

def ellipse_position(a_au, e, angle):
    a = a_au
    b = a * math.sqrt(1 - e*e)
    x = a * math.cos(angle) - a * e
    y = b * math.sin(angle)
    return (x, y, 0.0)  # z=0 plane
