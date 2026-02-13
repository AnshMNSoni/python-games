import sys
import os
import unittest
import math

# 🔴 ADD PROJECT ROOT TO PATH (CRITICAL)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from SolarSystemSimulator.logic import orbit_pts



class TestSolarSystem(unittest.TestCase):

    def test_orbit_returns_points(self):
        pts = orbit_pts(5)
        self.assertTrue(len(pts) > 0)

    def test_orbit_radius_correct(self):
        pts = orbit_pts(10)
        x, y, z = pts[0]
        r = math.sqrt(x*x + y*y)
        self.assertAlmostEqual(r, 10 * 7.4, delta=2)


if __name__ == "__main__":
    unittest.main()
