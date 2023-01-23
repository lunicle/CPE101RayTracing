import unittest
import data
import collisions

class TestCases(unittest.TestCase):

    def testintersection1(self):
        sphere = data.Sphere(data.Point(1, 1, 1), 1)
        ray = data.Ray(data.Point(1, 0, 0), data.Vector(0, 1, 0))
        point = data.Point(1, 1, 0)
        self.assertAlmostEqual(collisions.sphere_intersection_point(ray, sphere), point)

    def testintersection2(self):
        sphere = data.Sphere(data.Point(0, 0, 0), 2)
        ray = data.Ray(data.Point(3, 0, 0), data.Vector(-1, 0, 0))
        point = data.Point(2, 0, 0)
        self.assertAlmostEqual(collisions.sphere_intersection_point(ray, sphere), point)

    def testintersection3(self):
        sphere = data.Sphere(data.Point(1, 4, -3), 3)
        ray = data.Ray(data.Point(-10, 3, 5), data.Vector(1, 0, -1))
        point = data.Point(22.70849737787082, 3.0, -27.70849737787082)
        self.assertAlmostEqual(collisions.sphere_intersection_point(ray, sphere), point)

    def testlist(self):
        sphere1 = data.Sphere(data.Point(0, 0, 0), 2)
        sphere2 = data.Sphere(data.Point(0, 0, 0), 1)
        p1 = data.Point(-2, 0, 0)
        p2 = data.Point(-1, 0, 0)
        ray = data.Ray(data.Point(-3, 0, 0), data.Vector(1, 0, 0))
        results = [(sphere1,p1),(sphere2,p2)]
        self.assertAlmostEqual(collisions.find_intersection_points([sphere1, sphere2], ray), results)

    def testlist2(self):
        sphere1 = data.Sphere(data.Point(100, 0, 15), 20)
        sphere2 = data.Sphere(data.Point(0, 0, 4), 6)
        p1 = data.Point(86.77124344467705, 0, 0)
        p2 = data.Point(4.47213595499958, 0, 0)
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))
        results = [(sphere1,p1),(sphere2,p2)]
        self.assertAlmostEqual(collisions.find_intersection_points([sphere1, sphere2], ray), results)

    def testnorm(self):
            sphere = data.Sphere(data.Point(0, 0, 0), 1)
            point = data.Point(1, 0, 0)
            result = data.Vector(1, 0, 0)
            self.assertAlmostEqual(collisions.sphere_normal_at_point(sphere, point), result)
    def testnorm2(self):
            sphere = data.Sphere(data.Point(0, 0, 0), 5)
            point = data.Point(0, 5, 0)
            result = data.Vector(0, 1, 0)
            self.assertAlmostEqual(collisions.sphere_normal_at_point(sphere, point), result)


