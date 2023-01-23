import collisions
import data
import vector_math as vm

def cast_ray(ray, sphere_list, ambient_color,light):
    result = collisions.find_intersection_points(sphere_list,ray)
    if result == []:
        return data.Color(1.0,1.0,1.0)
    else:
        nearest = 0
        for i in range(len(result)):
            if vm.length_vector(vm.vector_from_to(ray.pt,result[i][1])) < vm.length_vector(vm.vector_from_to(ray.pt,result[nearest][1])):
                nearest = i
        near_sphere = result[nearest]
        ambient_r = result[nearest][0].color.r * ambient_color.r * result[nearest][0].finish.ambient
        ambient_g = result[nearest][0].color.g * ambient_color.g * result[nearest][0].finish.ambient
        ambient_b = result[nearest][0].color.b * ambient_color.b * result[nearest][0].finish.ambient

        N = collisions.sphere_normal_at_point(near_sphere[0], near_sphere[1])
        P_epsilon = vm.translate_point(near_sphere[1], vm.scale_vector(N, 0.01))
        light_dir = vm.normalize_vector(vm.vector_from_to(P_epsilon, light.pt))
        Pe_to_light_ray = data.Ray(P_epsilon,vm.vector_from_to(P_epsilon, light.pt))
        lightcollision = collisions.find_intersection_points(sphere_list, Pe_to_light_ray)
        if lightcollision == []:
            diffuse_factor = vm.dot_vector(N, light_dir) * near_sphere[0].finish.diffuse
        else:
            diffuse_factor = 0
        diffused_color_r = int(near_sphere[0].color.r * light.color.r) * diffuse_factor
        diffused_color_g = int(near_sphere[0].color.g * light.color.g) * diffuse_factor
        diffused_color_b = int(near_sphere[0].color.b * light.color.b) * diffuse_factor

        r = ambient_r + diffused_color_r
        g = ambient_g + diffused_color_g
        b = ambient_b + diffused_color_b

        return data.Color(r,g,b)

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
            result1 = cast_ray(pixel_ray,sphere_list, ambient_color,light)

            red = color_scale(result1.r)
            green = color_scale(result1.g)
            blue = color_scale(result1.b)
            print(red,green,blue)

def color_scale(check):
    c = check * 255
    if c <= 255:
        r = c
    else:
        r = 255
    return r