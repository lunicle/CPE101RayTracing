import vector_math
import math

def sphere_intersection_point(ray, sphere):
    difference = vector_math.difference_point(ray.pt, sphere.point)
    A = vector_math.dot_vector(ray.dir, ray.dir)
    B = (vector_math.dot_vector(vector_math.scale_vector(difference, 2), ray.dir))
    C1 = (vector_math.difference_point(ray.pt, sphere.point))
    C = ((vector_math.dot_vector(C1, C1)) - (sphere.radius ** 2))
    check = ((B*B) - (4*A*C))
    if check > 0:
        t2 = (-B - (math.sqrt(check)))/2*A
        scale = vector_math.scale_vector(ray.dir,t2)
        point_t = vector_math.translate_point(scale, ray.pt)
        return point_t
    elif check == 0:
        t2 = (-B + (math.sqrt(check))) / 2 * A
        scale = vector_math.scale_vector(ray.dir, t2)
        point_t = vector_math.translate_point(scale, ray.pt)
        return point_t
    else:
        return None

def find_intersection_points(sphere_list, ray):
    result = []
    for sphere in sphere_list:
        point = sphere_intersection_point(ray,sphere)
        if point is not None:
            result.append((sphere,point))
    return result

def sphere_normal_at_point(sphere, point):
    norm = vector_math.normalize_vector(vector_math.vector_from_to(sphere.point, point))
    return norm