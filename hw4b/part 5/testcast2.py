import data
import vector_math
import collisions

#own variables
near_sphere = 1
# returns color or closest sphere intersected, or the color white
def cast_ray(ray, sphere_list, ambient_color, light, eye_point):
    reslist = collisions.find_intersection_points(sphere_list, ray)

    if reslist == []:
        return data.Color(1, 1, 1)

    closest_sphere_pair = find_closest_sphere(ray.pt, reslist)
    sphere_color = closest_sphere_pair[0].color

    l_dot_n = vector_math.dot_vector(collisions.sphere_normal_at_point(closest_sphere_pair[0],closest_sphere_pair[1]),vector_math.normalize_vector(vector_math.difference_point(light.pt,closest_sphere_pair[1])))

    ambient_component = find_ambient_component(closest_sphere_pair[0], ambient_color)
    near_sphere = 1

    if light_hits_point(near_sphere, sphere_list, light):
        diffuse_component = find_diffuse_component(l_dot_n, light,near_sphere[0])

        newr = diffuse_component.r + ambient_component.r
        newg = diffuse_component.g + ambient_component.g
        newb = diffuse_component.b + ambient_component.b

        pixelcolor = data.Color(newr, newg, newb)
        # if color is past max/min, sets it to the max/min

    else:  # light doesn't hit ray
        newr = ambient_component.r
        newg = ambient_component.g
        newb = ambient_component.b

        pixelcolor = data.Color(newr, newg, newb)

    return pixelcolor



# helper functions
# returns the sphere pair with the closest point to the given point\

#JP checked
def find_closest_sphere(point, sphere_pair_list):
    if sphere_pair_list == []:
        return None
    closest = sphere_pair_list[0]
    distance = vector_math.distance(point, closest[1])
    for i in range(len(sphere_pair_list)):
        if vector_math.distance(point, sphere_pair_list[i][1]) < distance:
            closest = sphere_pair_list[i]
            distance = vector_math.distance(point, sphere_pair_list[i][1])
    return closest


# for computing light rays stuff
# finds point 0.01 off the sphere at the given point.
# used to prevent errors due to floating points

def P_epsilon(sphere, point): #P_epsilon
    normal_vector = collisions.sphere_normal_at_point(sphere, point)
    translate_vec = vector_math.scale_vector(normal_vector, 0.01)
    return vector_math.translate_point(point, translate_vec)


# returns true if the point is on the same side of the sphere
# as the light
def point_light_same_side(point, sphere, light):
    normal = collisions.sphere_normal_at_point(sphere, point) # omit
    pt_light_vec = vector_math.normalize_vector(vector_math.difference_point(light.pt, point))
    dot_product = vector_math.dot_vector(normal, pt_light_vec)
    if dot_product <= 0:
        return False
    else:
        return True


# returns true if there are no objects between the point and light
# including the sphere that contains the point
def point_unobstructed(point, light, sphere_list):
    light_dir = vector_math.normalize_vector(vector_math.difference_point(light.pt, point))
    ray_to_light = data.Ray(point, light_dir)
    spheres_intersected = collisions.find_intersection_points(sphere_list,ray_to_light)
    if spheres_intersected == []:
        return True
    else:
        return False


def light_hits_point(near_sphere, sphere_list, light):
    close_point = P_epsilon(near_sphere[0], near_sphere[1])
    return (point_light_same_side(close_point, near_sphere[0], light) and point_unobstructed(close_point, light, sphere_list))







#JP checked
def find_ambient_component(sphere, ambient_color):
    r = sphere.color.r * sphere.finish.ambient * ambient_color.r
    g = sphere.color.g * sphere.finish.ambient * ambient_color.g
    b = sphere.color.b * sphere.finish.ambient * ambient_color.b
    return data.Color(r, g, b)

#JP checked
def find_diffuse_component(l_dot_n, light, sphere):
    r = l_dot_n * light.color.r * sphere.color.r * sphere.finish.diffuse
    g = l_dot_n * light.color.g * sphere.color.g * sphere.finish.diffuse
    b = l_dot_n * light.color.b * sphere.color.b * sphere.finish.diffuse
    return data.Color(r, g, b)

