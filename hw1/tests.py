import unittest
import data

class TestCase(unittest.TestCase):
    def testpoint1(self):
        pt1 = data.Point(1, 5, 0)
        self.assertEqual(pt1.x,1)
        self.assertEqual(pt1.y,5)
        self.assertEqual(pt1.z,0)

    def testpoint2(self):
        pt1 = data.Point(113, 123, 1023)
        self.assertEqual(pt1.x, 113)
        self.assertEqual(pt1.y, 123)
        self.assertEqual(pt1.z, 1023)

    def testvector1(self):
        pt1 = data.Vector(1, 5, 10)
        self.assertAlmostEqual(pt1.x,1)
        self.assertAlmostEqual(pt1.y,5)
        self.assertAlmostEqual(pt1.z,10)

    def testvector2(self):
        pt1 = data.Vector(1.0, 0.5, 0.4)
        self.assertAlmostEqual(pt1.x, 1.0)
        self.assertAlmostEqual(pt1.y, 0.5)
        self.assertAlmostEqual(pt1.z, 0.4)

    def testray1(self):
        ray = data.Ray(data.Point(1, 2, 5), data.Vector(1.1, 2.2, 3.3))
        self.assertEqual(ray.pt.x,1)
        self.assertEqual(ray.pt.y,2)
        self.assertEqual(ray.pt.z,5)
        self.assertAlmostEqual(ray.dir.x,1.1)
        self.assertAlmostEqual(ray.dir.y, 2.2)
        self.assertAlmostEqual(ray.dir.z, 3.3)

    def testray2(self):
        ray = data.Ray(data.Point(2, 4, 6), data.Vector(1.0, 0.0, 0.0))
        self.assertEqual(ray.pt.x,2)
        self.assertEqual(ray.pt.y,4)
        self.assertEqual(ray.pt.z,6)
        self.assertAlmostEqual(ray.dir.x,1.0)
        self.assertAlmostEqual(ray.dir.y, 0.0)
        self.assertAlmostEqual(ray.dir.z, 0.0)

    def testSphere(self):
        center = data.Sphere(data.Point(0, 1, 0), 5)
        self.assertEqual(center.point.x,0)
        self.assertEqual(center.point.y,1)
        self.assertEqual(center.point.z,0)
        self.assertAlmostEqual(center.radius,5)

    def testSphere2(self):
        center = data.Sphere(data.Point(4, 5, 6), 2)
        self.assertEqual(center.point.x,4)
        self.assertEqual(center.point.y,5)
        self.assertEqual(center.point.z,6)
        self.assertAlmostEqual(center.radius,2)

#def spheretest(x,y,z,r):
    #pt = data.Sphere(data.Point(x,y,z),r)
    #return pt.radius

#print (spheretest(1,2,3,5))


if __name__ == "__main__":
    unittest.main()
