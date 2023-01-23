import unittest
import cast
import data

eye = data.Point(0,0,-14)
sphere1 = data.Sphere(data.Point(1,1,0),2,data.Color(0,0,1.0),data.Finish(0.2))
sphere2 = data.Sphere(data.Point(0.5,1.5,-3),0.5, data.Color(1.0,0,0),data.Finish(0.4))

min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 512
height = 384
ambient_color = data.Color(1.0,1.0,1.0)

cast.cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye,[sphere1,sphere2],ambient_color)