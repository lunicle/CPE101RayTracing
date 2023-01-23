import collisions
import data
import vector_math as vm

def cast_ray(ray, sphere_list):
    result = collisions.find_intersection_points(sphere_list,ray)
    if result == []:
        return data.Color(255,255,255)
    else:
        nearest = 0
        for i in range(len(result)):
            if vm.length_vector(vm.vector_from_to(ray.pt,result[i][1])) < vm.length_vector(vm.vector_from_to(ray.pt,result[nearest][1])):
                nearest = i
        return result[nearest][0].color

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list):
    print('P3')
    print(str(width) + ' ' + str(height))
    print('255')

    x_step = (max_x - min_x)/float(width)
    y_step = (max_y - min_y)/float(height)

    for yy in range(height):
        y = max_y - (yy * y_step)
        for xx in range(width):
            x = min_x + (xx * x_step)
            dir  = vm.vector_from_to(eye_point,data.Point(x,y,0))
            pixel_ray = data.Ray(eye_point, dir)
            result = cast_ray(pixel_ray,sphere_list)

            red = result.r
            print(red)
            green = result.g
            print(green)
            blue = result.b
            print(blue)
