import collisions
import data
import vector_math

def cast_ray(ray, sphere_list):
    result = collisions.find_intersection_points(sphere_list,ray)
    if len(result) > 0:
            return True

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list):
    print('P3')
    print(str(width) + ' ' + str(height))
    print('255')

    white = '0 0 0'
    black = '255 255 255'

    x_step = (max_x - min_x)/float(width)
    y_step = (max_y - min_y)/float(height)

    for yy in range(height):
        y = max_y - (yy * y_step)
        for xx in range(width):
            x = min_x + (xx * x_step)
            dir  = vector_math.vector_from_to(eye_point,data.Point(x,y,0))
            pixel_ray = data.Ray(eye_point, dir)
            result = collisions.find_intersection_points(sphere_list,pixel_ray)
            if len(result) > 0:
                print(white)
            else:
                print(black)