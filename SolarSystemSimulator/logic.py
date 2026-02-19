import math

DIST_SCALE = 7.4
ORBIT_STEPS = 260

def orbit_pts(a):
    pts = []
    for i in range(ORBIT_STEPS):
        ang = 2 * math.pi * i / ORBIT_STEPS
        x = a * math.cos(ang) * DIST_SCALE
        y = a * math.sin(ang) * DIST_SCALE
        z = 0.25 * a * math.sin(ang * 0.6)
        pts.append((x, y, z))
    return pts
