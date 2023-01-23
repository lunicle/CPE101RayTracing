import collisions
import data
import vector_math as vm

def cast_ray(ray, sphere_list, color):
    result = collisions.find_intersection_points(sphere_list,ray)
    if result == []:
        return data.Color(1.0,1.0,1.0)
    else:
        nearest = 0
        for i in range(len(result)):
            if vm.length_vector(vm.vector_from_to(ray.pt,result[i][1])) < vm.length_vector(vm.vector_from_to(ray.pt,result[nearest][1])):
                nearest = i
        r = result[nearest][0].color.r * color.r * result[nearest][0].finish.ambient
        g = result[nearest][0].color.g * color.g * result[nearest][0].finish.ambient
        b = result[nearest][0].color.b * color.b * result[nearest][0].finish.ambient
        return data.Color(r,g,b)


def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,color):
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
            result1 = cast_ray(pixel_ray,sphere_list, color)
            red = int(result1.r * 255)
            green = int(result1.g * 255)
            blue = int(result1.b * 255)
            print(red,green,blue)