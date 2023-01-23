import collisions
import data
import vector_math as vm

def cast_ray(ray, sphere_list, ambient_color,light, eye_point):
    result = collisions.find_intersection_points(sphere_list,ray)
    if result == []:
        return data.Color(1.0,1.0,1.0)
    else:
        nearest = 0
        for i in range(len(result)):
            if vm.length_vector(vm.vector_from_to(ray.pt,result[i][1])) < vm.length_vector(vm.vector_from_to(ray.pt,result[nearest][1])):
                nearest = i
        near_sphere = result[nearest]
        ambientcolor = ambient_color_function(near_sphere[0],ambient_color)

        P_epsilon = vm.translate_point(near_sphere[1], vm.scale_vector(collisions.sphere_normal_at_point(near_sphere[0],near_sphere[1]), 0.01))
        normal = collisions.sphere_normal_at_point(near_sphere[0],near_sphere[1])
        light_dir = vm.normalize_vector(vm.vector_from_to(P_epsilon,light.pt))
        visible = vm.dot_vector(normal,light_dir)
        reflection_vec = (vm.difference_vector(light_dir,vm.scale_vector(normal, (2*visible))))
        v_dir = vm.normalize_vector(vm.difference_point(P_epsilon,eye_point))
        spec = vm.dot_vector(reflection_vec,v_dir)

        if spec > 0:
            sr = light.color.r * near_sphere[0].finish.specular * spec ** (1 /near_sphere[0].finish.roughness)
            sg = light.color.g * near_sphere[0].finish.specular * spec ** (1 / near_sphere[0].finish.roughness)
            sb = light.color.b * near_sphere[0].finish.specular * spec ** (1 / near_sphere[0].finish.roughness)
        #i think my issue is with how I handle the color value. switching between 255 and 1.0 is too hard to track across different values that are given throughout the project.
        check = check_light_collision(P_epsilon,light_dir,sphere_list)
        if check == False:
            diffusecolor = diffuse_color_function(visible,light,near_sphere[0])
            r_final = ambientcolor.r + diffusecolor.r
            g_final = ambientcolor.g + diffusecolor.g
            b_final = ambientcolor.b + diffusecolor.b
            pixel_color = data.Color(r_final,g_final,b_final)
        else:
            r_final = ambientcolor.r
            g_final = ambientcolor.g
            b_final = ambientcolor.b
            pixel_color = data.Color(r_final, g_final, b_final)

        srfinal = pixel_color.r + sr
        sgfinal = pixel_color.g + sg
        sbfinal = pixel_color.b + sb
    return data.Color(srfinal,sgfinal,sbfinal)

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient_color,light):
    print('P3')
    print(str(width) + ' ' + str(height))
    print('255')

    white = '255 0 0'
    black = '0 0 0'

    x_step = (max_x - min_x)/float(width)
    y_step = (max_y - min_y)/float(height)

    for yy in range(height):
        y = max_y - (yy * y_step)
        for xx in range(width):
            x = min_x + (xx * x_step)
            dir  = vm.vector_from_to(eye_point,data.Point(x,y,0))
            pixel_ray = data.Ray(eye_point, dir)
            result1 = cast_ray(pixel_ray,sphere_list, ambient_color,light, eye_point)

            red = color_scale(result1.r)
            green = color_scale(result1.g)
            blue = color_scale(result1.b)
            print(red,green,blue)

def color_scale(check):
    c = int(check * 255)
    if c <= 255:
        r = c
    else:
        r = 255
    return r

def ambient_color_function(sphere,ambient_color):
    r = sphere.color.r * ambient_color.r * sphere.finish.ambient
    g = sphere.color.g * ambient_color.g * sphere.finish.ambient
    b = sphere.color.b * ambient_color.b * sphere.finish.ambient
    return data.Color(r,g,b)

def check_same_side(normal,light_dir):
    check = vm.dot_vector(normal,light_dir)
    if check < 0:
        return False
    else:
        return True

def check_light_collision(P_epsilon,light_dir,sphere_list):
    ray2light = data.Ray(P_epsilon,light_dir)
    result = collisions.find_intersection_points(sphere_list,ray2light)
    if result == []:
        return False
    else:
        return True


def diffuse_color_function(visible, light,sphere):
    r = visible * light.color.r * sphere.color.r * sphere.finish.diffuse
    g = visible * light.color.g * sphere.color.g * sphere.finish.diffuse
    b = visible * light.color.b * sphere.color.b * sphere.finish.diffuse
    return data.Color(r,g,b)
