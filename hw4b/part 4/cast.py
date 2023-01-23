import collisions
import data
import vector_math as vm

def cast_ray(ray, sphere_list, ambient_color,light):
    result = collisions.find_intersection_points(sphere_list, ray)
    if result == []:
        return data.Color(1.0, 1.0, 1.0)
    else:
        nearest = 0
        for i in range(len(result)):
            if vm.length_vector(vm.vector_from_to(ray.pt,result[i][1])) < vm.length_vector(vm.vector_from_to(ray.pt,result[nearest][1])):
                nearest = i
            r = result[nearest][0].color.r * ambient_color.r * result[nearest][0].finish.ambient
            g = result[nearest][0].color.g * ambient_color.g * result[nearest][0].finish.ambient
            b = result[nearest][0].color.b * ambient_color.b * result[nearest][0].finish.ambient

        N = collisions.sphere_normal_at_point(result[nearest][0], result[nearest][1])
        Pe = vm.translate_point(result[nearest][1],vm.scale_vector(N,0.01))
        light_dir = vm.normalize_vector(vm.vector_from_to(Pe,light.pt))
        visible = vm.dot_vector(light_dir, collisions.sphere_normal_at_point(result[nearest][0], Pe))
        lightcollision = collisions.find_intersection_points(sphere_list, data.Ray(Pe,light_dir))
        if lightcollision == []:
            diffuse_factor = visible * result[nearest][0].finish.diffuse
            diffuse_color_r = int(result[nearest][0].color.r * light.color.r) * diffuse_factor
            diffuse_color_g = int(result[nearest][0].color.g * light.color.g) * diffuse_factor
            diffuse_color_b = int(result[nearest][0].color.b * light.color.b) * diffuse_factor
            diffuse_color = data.Color(diffuse_color_r, diffuse_color_g, diffuse_color_b)
        else:
            diffuse_factor = 0
            diffuse_color_r = int(result[nearest][0].color.r * light.color.r) * diffuse_factor
            diffuse_color_g = int(result[nearest][0].color.g * light.color.g) * diffuse_factor
            diffuse_color_b = int(result[nearest][0].color.b * light.color.b) * diffuse_factor
            return data.Color(diffuse_color_r, diffuse_color_g, diffuse_color_b)
        r_final = r + diffuse_color.r
        g_final = g + diffuse_color.g
        b_final = b + diffuse_color.b
        return data.Color(r_final,g_final,b_final)

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient_color,light):
    print('P3')
    print(str(width) + ' ' + str(height))
    print('255')

    x_step = (max_x - min_x)/float(width)
    y_step = (max_y - min_y)/float(height)

    for yy in range(height):
        y = max_y - (yy * y_step)
        for xx in range(width):
            x = min_x + (xx * x_step)
            dir = vm.vector_from_to(eye_point, data.Point(x, y, 0))
            pixel_ray = data.Ray(eye_point, dir)
            result1 = cast_ray(pixel_ray, sphere_list, ambient_color, light)

            red = check_color(result1.r * 255)

            green = check_color(result1.g * 255)

            blue = check_color(result1.b * 255)
            print(red,green,blue)

def check_color(check):
    if check <= 255:
        r = check
    else:
        r = 255
    return r

def nearest_sphere(ray,sphere_list):
    result = collisions.find_intersection_points(sphere_list, ray)
    nearest = 0
    for i in range(len(result)):
        if vm.length_vector(vm.vector_from_to(ray.pt, result[i][1])) < vm.length_vector(vm.vector_from_to(ray.pt, result[nearest][1])):
            nearest = i
    return result[nearest]