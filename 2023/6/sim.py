from vpython import *
import numpy as np
import time as tm

x1, y1, x2, y2, x3, y3 = 5, 3, -3, 3, -3, -5
v, t, w = 15, 4, 20
# x1, y1, x2, y2, x3, y3 = 10, 0, 0, 5, -7, -7
# v, t, w = 30, 20, 50
# x1, y1, x2, y2, x3, y3 = 5, 3, -3, 3, -3, -5
# v, t, w = 15, 4, 20

scene = canvas(autoscale = False)
scene.camera.pos = vec(30, 0, 40)
triangle = triangle(v0=vertex(pos=vec(x1, y1, 0)), v1=vertex(pos=vec(x2, y2, 0)), v2=vertex(pos=vec(x3, y3, 0)))

p1 = graph(title = 'Point 1', xtitle = 'X', ytitle='Y')
p1c = gcurve(graph = p1, color = color.red)
p2 = graph(title = 'Point 2', xtitle = 'X', ytitle='Y')
p2c = gcurve(graph = p2, color = color.red)
p3 = graph(title = 'Point 3', xtitle = 'X', ytitle='Y')
p3c = gcurve(graph = p3, color = color.red)


r1 = sqrt(x1 ** 2 + y1 ** 2)
r2 = sqrt(x2 ** 2 + y2 ** 2)
r3 = sqrt(x3 ** 2 + y3 ** 2)
dpt = 360 / t  # this is the amount of degrees it goes for every t
com = 0
time = 0
dtime = 0.01
d_angle = dpt * dtime
dx = dtime * v

def rotate(d_angle, x, y, r):
    x = (x - com)
    if x < 0:
        d_angle += 180
    a_r = (d_angle * np.pi) / 180
    if x == 0:
        di = y / np.inf
    else:
        di = y / x
    n = a_r + (np.arctan(di))
    n_x = (r * cos(n)) + com
    n_y = r * sin(n)
    return vertex(pos=vec(n_x, n_y, 0))

def translate(dx, pos):
    return vertex(pos=vec(pos.x + dx, pos.y, pos.z))

def has_touched(tri, time):
    if tri.v0.pos.x >= w or tri.v1.pos.x >= w or tri.v2.pos.x >= w:
        print(time)
        return True
    return False

while time < 4: # not has_touched(triangle, time):
    tm.sleep(0.001)
    triangle.v0 = rotate(d_angle, triangle.v0.pos.x, triangle.v0.pos.y, r1)
    triangle.v1 = rotate(d_angle, triangle.v1.pos.x, triangle.v1.pos.y, r2)
    triangle.v2 = rotate(d_angle, triangle.v2.pos.x, triangle.v2.pos.y, r3)
    triangle.v0 = translate(dx, triangle.v0.pos)
    triangle.v1 = translate(dx, triangle.v1.pos)
    triangle.v2 = translate(dx, triangle.v2.pos)
    
    p1c.plot(pos=(triangle.v0.pos.x, triangle.v0.pos.y))
    p2c.plot(pos=(triangle.v1.pos.x, triangle.v1.pos.y))
    p3c.plot(pos=(triangle.v2.pos.x, triangle.v2.pos.y))
    
    com += dx
    time += dtime


