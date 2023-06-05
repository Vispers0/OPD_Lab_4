import unittest

from main import *
import math


class TestMethods(unittest.TestCase):

    def test_cube(self):
        self.assertEqual(cube(5, 3), round(5 ** 3, 3))
        self.assertEqual(cube(1, 3), 1)
        self.assertEqual(cube(0, 3), 0)
        self.assertEqual(cube(2, 0), round(2 ** 3, 0))
        self.assertEqual(cube(43.567, 6), round(43.567 ** 3, 6))

    def test_cube_values(self):
        self.assertRaises(ValueError, cube, -1, 5)
        self.assertRaises(ValueError, cube, -4, 0)

    def test_cube_type(self):
        self.assertRaises(TypeError, cube, 'sheesh', 'yeet')
        self.assertRaises(TypeError, cube, 5+3j, 7+1j)
        self.assertRaises(TypeError, cube, True, False)
        self.assertRaises(TypeError, cube, [12, 45, 53, True, "killa"], 5)
        self.assertRaises(TypeError, cube)

    def test_prism(self):
        self.assertEqual(prism(50.4, 15, 4), round(50.4 * 15, 4))
        self.assertEqual(prism(1, 1, 0), 1)
        self.assertEqual(prism(0, 0, 0), 0)
        self.assertEqual(prism(2, 0.5, 0), round(2 * 0.5, 0))
        self.assertEqual(prism(43.56712, 987.56412, 6), round(43.56712 * 987.56412, 6))

    def test_prism_values(self):
        self.assertRaises(ValueError, prism, -1, 5, 1)
        self.assertRaises(ValueError, prism, -4, 0, 0)

    def test_prism_type(self):
        self.assertRaises(TypeError, prism, 'sheesh', 'yeet', 'aaa')
        self.assertRaises(TypeError, prism, 5+3j, 7+1j, 4)
        self.assertRaises(TypeError, prism, True, False, None)
        self.assertRaises(TypeError, prism, [12, 45, 53, True, "killa"], 5, None)
        self.assertRaises(TypeError, prism)

    def test_parallel(self):
        self.assertEqual(prism(50.4, 15, 4), round(50.4 * 15, 4))
        self.assertEqual(prism(1, 1, 0), 1)
        self.assertEqual(prism(0, 0, 0), 0)
        self.assertEqual(prism(2, 0.5, 0), round(2 * 0.5, 0))
        self.assertEqual(prism(43.56712, 987.56412, 6), round(43.56712 * 987.56412, 6))

    def test_parallel_values(self):
        self.assertRaises(ValueError, prism, -1, 5, 1)
        self.assertRaises(ValueError, prism, -4, 0, 0)

    def test_parallel_type(self):
        self.assertRaises(TypeError, prism, 'sheesh', 'yeet', 'aaa')
        self.assertRaises(TypeError, prism, 5 + 3j, 7 + 1j, 4)
        self.assertRaises(TypeError, prism, True, False, None)
        self.assertRaises(TypeError, prism, [12, 45, 53, True, "killa"], 5, None)
        self.assertRaises(TypeError, prism)

    def test_rect_parallel(self):
        self.assertEqual(rect_parallel(50.4, 15, 4, 4), round(50.4 * 15 * 4, 4))
        self.assertEqual(rect_parallel(1, 1, 1, 0), 1)
        self.assertEqual(rect_parallel(0, 0, 0, 0), 0)
        self.assertEqual(rect_parallel(2, 0.5, 0.897, 0), round(2 * 0.5 * 0.897, 0))
        self.assertEqual(rect_parallel(43.56712, 987.56412, 1.8979, 6), round(43.56712 * 987.56412 * 1.8979, 6))

    def test_rect_parallel_values(self):
        self.assertRaises(ValueError, rect_parallel, -1, 5, -5.4, -1)
        self.assertRaises(ValueError, rect_parallel, -4, 0, -56, 4)

    def test_rect_parallel_type(self):
        self.assertRaises(TypeError, rect_parallel, 'sheesh', 'yeet', 'aaa', 7)
        self.assertRaises(TypeError, rect_parallel, 5+3j, 7+1j, 4, 5+6j)
        self.assertRaises(TypeError, rect_parallel, True, False, None, True)
        self.assertRaises(TypeError, rect_parallel, [12, 45, 53, True, "killa"], 5, None, False)
        self.assertRaises(TypeError, rect_parallel)

    def test_pyramid(self):
        self.assertEqual(pyramid(50.4, 15, 4), round((1/3) * 50.4 * 15, 4))
        self.assertEqual(pyramid(1, 1, 0), round((1/3) * 1 * 1, 0))
        self.assertEqual(pyramid(0, 0, 0), 0)
        self.assertEqual(pyramid(2, 0.5, 0), round((1/3) * 2 * 0.5, 0))
        self.assertEqual(pyramid(43.56712, 987.56412, 6), round((1/3) * 43.56712 * 987.56412, 6))

    def test_pyramid_values(self):
        self.assertRaises(ValueError, pyramid, -1, 5, 1)
        self.assertRaises(ValueError, pyramid, -4, 0, 0)

    def test_pyramid_type(self):
        self.assertRaises(TypeError, pyramid, 'sheesh', 'yeet', 'aaa')
        self.assertRaises(TypeError, pyramid, 5+3j, 7+1j, 4)
        self.assertRaises(TypeError, pyramid, True, False, None)
        self.assertRaises(TypeError, pyramid, [12, 45, 53, True, "killa"], 5, None)
        self.assertRaises(TypeError, pyramid)

    def test_tetra(self):
        self.assertEqual(tetra(5, 3), round((5 ** 3 * math.sqrt(2)) / 12, 3))
        self.assertEqual(tetra(1, 3), round((1 ** 3 * math.sqrt(2)) / 12, 3))
        self.assertEqual(tetra(0, 3), 0)
        self.assertEqual(tetra(2, 0), round((2 ** 3 * math.sqrt(2)) / 12, 0))
        self.assertEqual(tetra(43.567, 6), round((43.567 ** 3 * math.sqrt(2)) / 12, 6))

    def test_tetra_values(self):
        self.assertRaises(ValueError, tetra, -1, 5)
        self.assertRaises(ValueError, tetra, -4, 0)

    def test_tetra_type(self):
        self.assertRaises(TypeError, tetra, 'sheesh', 'yeet')
        self.assertRaises(TypeError, tetra, 5+3j, 7+1j)
        self.assertRaises(TypeError, tetra, True, False)
        self.assertRaises(TypeError, tetra, [12, 45, 53, True, "killa"], 5)
        self.assertRaises(TypeError, tetra)

    def test_cylinder(self):
        self.assertEqual(cylinder(50.4, 15, 4), round(pi * 50.4 ** 2 * 15, 4))
        self.assertEqual(cylinder(1, 1, 0), round(pi * 1 ** 2 * 1, 0))
        self.assertEqual(cylinder(0, 0, 0), 0)
        self.assertEqual(cylinder(2, 0.5, 0), round(pi * 2 ** 2 * 0.5, 0))
        self.assertEqual(cylinder(43.56712, 987.56412, 6), round(pi * 43.56712 ** 2 * 987.56412, 6))

    def test_cylinder_values(self):
        self.assertRaises(ValueError, cylinder, -1, 5, 1)
        self.assertRaises(ValueError, cylinder, -4, 0, 0)

    def test_cylinder_type(self):
        self.assertRaises(TypeError, cylinder, 'sheesh', 'yeet', 'aaa')
        self.assertRaises(TypeError, cylinder, 5+3j, 7+1j, 4)
        self.assertRaises(TypeError, cylinder, True, False, None)
        self.assertRaises(TypeError, cylinder, [12, 45, 53, True, "killa"], 5, None)
        self.assertRaises(TypeError, cylinder)

    def test_cone(self):
        self.assertEqual(cone(50.4, 15, 4), round((1/3) * pi * 50.4 ** 2 * 15, 4))
        self.assertEqual(cone(1, 1, 0), round((1/3) * pi * 1 ** 2 * 1, 0))
        self.assertEqual(cone(0, 0, 0), 0)
        self.assertEqual(cone(2, 0.5, 0), round((1/3) * pi * 2 ** 2 * 0.5, 0))
        self.assertEqual(cone(43.56712, 987.56412, 6), round((1/3) * pi * 43.56712 ** 2 * 987.56412, 6))

    def test_cone_values(self):
        self.assertRaises(ValueError, cone, -1, 5, 1)
        self.assertRaises(ValueError, cone, -4, 0, 0)

    def test_cone_type(self):
        self.assertRaises(TypeError, cone, 'sheesh', 'yeet', 'aaa')
        self.assertRaises(TypeError, cone, 5+3j, 7+1j, 4)
        self.assertRaises(TypeError, cone, True, False, None)
        self.assertRaises(TypeError, cone, [12, 45, 53, True, "killa"], 5, None)
        self.assertRaises(TypeError, cone)

    def test_ball(self):
        self.assertEqual(ball(5, 3), round((4/3) * pi * 5 ** 3, 3))
        self.assertEqual(ball(1, 3), round((4/3) * pi * 1 ** 3, 3))
        self.assertEqual(ball(0, 3), 0)
        self.assertEqual(ball(2, 0), round((4/3) * pi * 2 ** 3, 0))
        self.assertEqual(ball(43.567, 6), round((4/3) * pi * 43.567 ** 3, 6))

    def test_ball_values(self):
        self.assertRaises(ValueError, ball, -1, 5)
        self.assertRaises(ValueError, ball, -4, 0)

    def test_ball_type(self):
        self.assertRaises(TypeError, ball, 'sheesh', 'yeet')
        self.assertRaises(TypeError, ball, 5+3j, 7+1j)
        self.assertRaises(TypeError, ball, True, False)
        self.assertRaises(TypeError, ball, [12, 45, 53, True, "killa"], 5)
        self.assertRaises(TypeError, ball)


if __name__ == '__main__':
    unittest.main()
