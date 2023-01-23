import collisions
import data
import vector_math as vm

def cast_ray(ray, sphere_list, color,light):
    c = collisions.find_intersection_points(sphere_list, ray)
    if c == []:
        return data.Color(1.0, 1.0, 1.0)
    else:
        nearest = 0
        for i in range(len(c)):
            if vm.length_vector(vm.vector_from_to(ray.pt, c[i][1])) < vm.length_vector(vm.vector_from_to(ray.pt, c[nearest][1])):
                nearest = i
            r = c[nearest][0].color.r * color.r * c[nearest][0].finish.ambient
            g = c[nearest][0].color.g * color.g * c[nearest][0].finish.ambient
            b = c[nearest][0].color.b * color.b * c[nearest][0].finish.ambient

        Pe = vm.translate_point(c[nearest][1], vm.scale_vector(
            collisions.sphere_normal_at_point(c[nearest][0], c[nearest][1]), 0.01))
        light_dir = vm.normalize_vector(vm.vector_from_to(Pe, light.pt))
        visible = vm.dot_vector(light_dir, collisions.sphere_normal_at_point(c[nearest][0], Pe))
        ray_col = data.Ray(Pe, vm.vector_from_to(Pe, light.pt))

        if visible > 0:
            c1 = collisions.find_intersection_points(sphere_list, ray_col)
            if c1 == []:
                r += light.color.r * visible * c[nearest][0].finish.diffuse * c[nearest][0].color.r
                b += light.color.b * visible * c[nearest][0].finish.diffuse * c[nearest][0].color.b
                g += light.color.g * visible * c[nearest][0].finish.diffuse * c[nearest][0].color.g
        return data.Color(r, g, b)

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,color,light):
    print('P3')
    print(str(width) + ' ' + str(height))
    print('255')

    x_step = (max_x - min_x)/float(width)
    y_step = (max_y - min_y)/float(height)

    for yy in range(height):
        y = max_y - (yy * y_step)
        for xx in range(width):
            x = min_x + (xx * x_step)
            dir  = vm.vector_from_to(eye_point, data.Point(x, y, 0))
            pixel_ray = data.Ray(eye_point, dir)
            result1 = cast_ray(pixel_ray,sphere_list, color,light)

            red = scaler(result1.r)
            print(red)
            green = scaler(result1.g)
            print(green)
            blue = scaler(result1.b)
            print(blue)

def scaler(check):
    result = int(check * 255)
    if result > 255:
        result = 255
    return result