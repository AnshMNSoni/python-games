# =============================
# SAFE IMPORTS (logic only)
# =============================

from vpython import *
import time, math, random, os
import planets as P


# -----------------------------
# CONSTANTS (safe)
# -----------------------------

TIME_SPEED = 7.0
ROT_SPEED = 0.003
DIST_SCALE = 7.4
TRAIL_LEN = 220
ORBIT_STEPS = 260


# -----------------------------
# HELPERS (safe)
# -----------------------------

def rgb255(r, g, b):
    return vector(r/255, g/255, b/255)


from .logic import orbit_pts

    """Pure math → SAFE for testing"""
    pts = []
    for i in range(ORBIT_STEPS):
        ang = 2 * math.pi * i / ORBIT_STEPS
        x = a * math.cos(ang) * DIST_SCALE
        y = a * math.sin(ang) * DIST_SCALE
        z = 0.25 * a * math.sin(ang * 0.6)
        pts.append((x, y, z))  # return tuple (not vector) → easier for tests
    return pts


# -----------------------------
# BODY STATE CLASS (safe)
# -----------------------------

class BodyState:
    def __init__(self, body):
        self.body = body
        self.angle = random.random() * 2 * math.pi
        self.pos = vector(0, 0, 0)
        self.sphere = None
        self.label = None
        self.trail = None
        self.orbit = None
        self.children = []


# =========================================================
# EVERYTHING BELOW = GRAPHICS / SIMULATION (NOT SAFE)
# =========================================================

def run_simulation():

    # -----------------------------
    # Scene setup
    # -----------------------------

    scene.title = "Solar System 3D — Ultimate Edition"
    scene.width = 1280
    scene.height = 800
    scene.background = color.black
    scene.forward = vector(-1.4, -0.45, -2.4)
    scene.userspin = True
    scene.userzoom = True
    scene.range = 70

    local_light(pos=vector(0,0,0), color=vector(1.0,0.97,0.85))
    distant_light(direction=vector(1,-0.2,-0.4), color=vector(0.35,0.35,0.35))

    # -----------------------------
    # Stars
    # -----------------------------

    for _ in range(700):
        sphere(
            pos=vector(random.uniform(-420,420),
                       random.uniform(-420,420),
                       random.uniform(-420,420)),
            radius=0.9,
            color=color.white,
            emissive=True
        )

    # -----------------------------
    # Create bodies
    # -----------------------------

    states = {b.name: BodyState(b) for b in P.BODIES}

    for b in P.BODIES:
        if b.parent:
            states[b.parent].children.append(b.name)

    sun = states["Sun"]
    sun.sphere = sphere(pos=vector(0,0,0), radius=2.6,
                        color=color.yellow, emissive=True)

    # -----------------------------
    # Update logic
    # -----------------------------

    def update_body(name, parent_pos, dt):
        st = states[name]
        b = st.body

        if name == "Sun":
            st.pos = vector(0,0,0)
        else:
            w = (2*math.pi/b.period_days)*0.4
            st.angle += w * (dt*TIME_SPEED)

            x = b.au*math.cos(st.angle)*DIST_SCALE
            y = b.au*math.sin(st.angle)*DIST_SCALE

            st.pos = parent_pos + vector(x,y,0)

        st.sphere.pos = st.pos

        for child in st.children:
            update_body(child, st.pos, dt)

    # -----------------------------
    # MAIN LOOP
    # -----------------------------

    prev = time.time()

    while True:
        rate(60)

        now = time.time()
        dt = now - prev
        prev = now

        update_body("Sun", vector(0,0,0), dt)


# =========================================================
# ENTRY POINT (CRITICAL)
# =========================================================

if __name__ == "__main__":
    run_simulation()
