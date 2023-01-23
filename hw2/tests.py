import unittest
import data
import vector_math

class TestCases(unittest.TestCase):
    def testpoint1(self):
        pt1= data.Point(1, 2, 3)
        pt2= data.Point(1, 2, 3)
        pt3= data.Point(2, 3, 4)
        self.assertTrue(pt1 == pt2)
        self.assertFalse(pt1 == pt3)
    def testpoint2(self):
        pt1 = data.Point(2, 4, 6)
        pt2 = data.Point(2, 4, 6)
        pt3 = data.Point(1, 2, 3)
        self.assertTrue(pt1 == pt2)
        self.assertFalse(pt1 == pt3)
    def testvector1(self):
        pt1 = data.Point(1, 2, 3)
        pt2 = data.Point(2, 4, 6)
        pt3 = data.Point(1, 2, 3)
        self.assertTrue(pt1 == pt3)
        self.assertFalse(pt1 == pt2)

    def testvector2(self):
        pt1 = data.Point(342, 543, 654)
        pt2 = data.Point(342, 543, 654)
        pt3 = data.Point(1, 2, 3)
        self.assertTrue(pt1 == pt2)
        self.assertFalse(pt1 == pt3)
#------------------------------------------------------------------------
    def testscale1(self):
        pt1 = data.Vector(1, 2, 3)
        scalar = 2
        v = vector_math.scale_vector(pt1, scalar)
        self.assertAlmostEqual(v.x, 2)
        self.assertAlmostEqual(v.y, 4)
        self.assertAlmostEqual(v.z, 6)

    def testscale2(self):
        pt1 = data.Vector(1, 3, 5)
        scalar = 3
        v = vector_math.scale_vector(pt1, scalar)
        self.assertAlmostEqual(v.x, 3)
        self.assertAlmostEqual(v.y, 9)
        self.assertAlmostEqual(v.z, 15)

    def testdotvector1(self):
        pt1 = data.Vector(1, 2, 3)
        pt2 = data.Vector(2, 4, 6)
        v = vector_math.dot_vector(pt1, pt2)
        self.assertAlmostEqual(v, 28)

    def testdotvector2(self):
        pt1 = data.Vector(1, 3, 5)
        pt2 = data.Vector(2, 3, 4)
        v = vector_math.dot_vector(pt1, pt2)
        self.assertAlmostEqual(v, 31)

    def testlengthvector1(self):
        pt1 = data.Vector(3, 2, 4)
        final = vector_math.length_vector(pt1)
        self.assertAlmostEqual(final,5.385164807)

    def testlengthvector2(self):
        pt1 = data.Vector(2, 4, 6)
        final = vector_math.length_vector(pt1)
        self.assertAlmostEqual(final,7.48331477)

    def testnormalizevector1(self):
        pt1 = data.Vector(3, 2, 4)
        final = vector_math.normalize_vector(pt1)
        self.assertAlmostEqual(final.x,0.5570860145)
        self.assertAlmostEqual(final.y, 0.3713906764)
        self.assertAlmostEqual(final.z, 0.7427813527)

    def testnormalizevector2(self):
        pt1 = data.Vector(2, 4, 6)
        final = vector_math.normalize_vector(pt1)
        self.assertAlmostEqual(final.x,0.2672612419)
        self.assertAlmostEqual(final.y, 0.5345224838)
        self.assertAlmostEqual(final.z, 0.8017837257)

    def testdifference1(self):
        pt1 = data.Point(1, 2, 3)
        pt2 = data.Point(2, 4, 6)
        final = vector_math.difference_point(pt1, pt2)
        self.assertAlmostEqual(final.x,-1)
        self.assertAlmostEqual(final.y, -2)
        self.assertAlmostEqual(final.z, -3)

    def testdifference2(self):
        pt1 = data.Point(2, 4, 6)
        pt2 = data.Point(1, 10, 2)
        final = vector_math.difference_point(pt1, pt2)
        self.assertAlmostEqual(final.x,1)
        self.assertAlmostEqual(final.y, -6)
        self.assertAlmostEqual(final.z, 4)

    def testdifferencevector1(self):
        pt1 = data.Vector(2, 5, 6)
        pt2 = data.Vector(1, 10, 7)
        final = vector_math.difference_vector(pt1, pt2)
        self.assertAlmostEqual(final.x, 1)
        self.assertAlmostEqual(final.y, -5)
        self.assertAlmostEqual(final.z, 1)

    def testdifferencevector1(self):
        pt1 = data.Vector(4, 6, 10)
        pt2 = data.Vector(1, 10, 2)
        final = vector_math.difference_vector(pt1, pt2)
        self.assertAlmostEqual(final.x, 3)
        self.assertAlmostEqual(final.y, -4)
        self.assertAlmostEqual(final.z, 8)

    def testtranslate1(self):
        pt1 = data.Point(1, 2, 3)
        v1 = data.Vector(2, 4, 5)
        final = vector_math.translate_point(pt1, v1)
        self.assertAlmostEqual(final.x, 3)
        self.assertAlmostEqual(final.y,6)
        self.assertAlmostEqual(final.z,8)

    def testtranslate2(self):
        pt1 = data.Point(2, 7, 9)
        v1 = data.Vector(1, 3, 5)
        final = vector_math.translate_point(pt1, v1)
        self.assertAlmostEqual(final.x, 3)
        self.assertAlmostEqual(final.y,10)
        self.assertAlmostEqual(final.z,14)

    def testtofrom1(self):
        pt1 = data.Point(4, 5, 6)
        pt2 = data.Point(5, 7, 10)
        final = vector_math.vector_from_to(pt1, pt2)
        self.assertAlmostEqual(final.x, 1)
        self.assertAlmostEqual(final.y,2)
        self.assertAlmostEqual(final.z,4)

    def testtofrom2(self):
        pt1 = data.Point(2, 15, 50)
        pt2 = data.Point(1, 20, 100)
        final = vector_math.vector_from_to(pt1, pt2)
        self.assertAlmostEqual(final.x, -1)
        self.assertAlmostEqual(final.y,5)
        self.assertAlmostEqual(final.z,50)




