import data
import math


def scale_vector(vector, scalar):
    vx = (vector.x)*scalar
    vy = (vector.y)*scalar
    vz = (vector.z)*scalar
    vectorfinal = data.Vector(vx, vy, vz)
    return vectorfinal

def dot_vector(vector1, vector2):
    vx = vector1.x * vector2.x
    vy = vector1.y * vector2.y
    vz = vector1.z * vector2.z
    vectorfinal =  vx+vy+vz
    return vectorfinal

def length_vector(vector):
    d1 = math.sqrt(((vector.x)**2)+((vector.z)**2))
    magnitude = math.sqrt(((vector.y)**2)+(d1**2))
    return magnitude

def normalize_vector(vector):
    d1 = math.sqrt(((vector.x) ** 2) + ((vector.z) ** 2))
    magnitude = math.sqrt(((vector.y) ** 2) + (d1 ** 2))
    s = 1/magnitude
    vectorfinal = data.Vector(((vector.x) * s), ((vector.y) * s), ((vector.z) * s))
    return vectorfinal

def difference_point(point1, point2):
    c = data.Vector((point1.x - point2.x), (point1.y - point2.y), (point1.z - point2.z))
    return c

def difference_vector(vector1, vector2):
    c = data.Vector((vector1.x - vector2.x), (vector1.y - vector2.y), (vector1.z - vector2.z))
    return c

def translate_point(point, vector):
    pfinal =  data.Point((point.x + vector.x), (point.y + vector.y), (point.z + vector.z))
    return pfinal

def vector_from_to(from_point, to_point):
    c = data.Vector((to_point.x - from_point.x), (to_point.y - from_point.y), (to_point.z - from_point.z))
    return c

