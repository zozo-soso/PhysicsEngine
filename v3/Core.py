import Extras,Objects
from math import inf, sin, cos, sqrt, tan, atan2,pi


class System():
    stop = False
    pause = False
    objects = []
    walls = []
    relations = {}
    collisions = []
    pumbs = []
    # collision_time=[]       i will not use right now instead
    # co_t=1
    t = 0

    def __init__(self, duration, fps, lengthx, lengthy):

        self.duration = duration
        self.fps = fps
        self.lengthx = lengthx
        self.lengthy = lengthy

        self.add_wall(Objects.Wall(0,0,0,lengthy,_type='border'))
        self.add_wall(Objects.Wall(0,0,lengthx,0,_type='border'))
        self.add_wall(Objects.Wall(0,lengthy,lengthx,lengthy,_type='border'))
        self.add_wall(Objects.Wall(lengthx,0,lengthx,lengthy,_type='border'))
    def run(self):
        for i in range(len(self.objects)):
            for j in range(i+1,len(self.objects)):
                self.relations[self.objects[i],self.objects[j]]=False
            for j in range(len(self.walls)):
                self.relations[self.objects[i],self.walls[j]]=False
    def update(self):
        self.t += 1/self.fps
        for obj in self.objects:
            obj.move(1/self.fps)
        self.collision_check()

    def is_running(self):
        return (not self.stop) and (self.t < self.duration)  # including updating

    def add_object(self, obj):
        self.objects.append(obj)

    def add_wall(self, wall):
        self.walls.append(wall)

    def distance1(self, x1, y1, x2, y2):
        return (sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))

    #def distance2(self, wall, point):
    #    x1 = wall.x1;
    #    x2 = wall.x2;
    #    y1 = wall.y1;
    #    y2 = wall.y2;
    #    x0 = point.px;
    #    y0 = point.py;
    #    return (abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - x1 * y2) / self.distance1(x1, y1, x2, y2))

    def distance2(self, wall, point):
        x1, y1, x2, y2 = wall.x1, wall.y1, wall.x2, wall.y2
        x0, y0 = point.px, point.py
        dx, dy = x2 - x1, y2 - y1
        if dx == 0 and dy == 0:
            # wall is a point
            return sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
        t = ((x0 - x1) * dx + (y0 - y1) * dy) / (dx * dx + dy * dy)
        if t < 0:
            cx, cy = x1, y1
        elif t > 1:
            cx, cy = x2, y2
        else:
            cx, cy = x1 + t * dx, y1 + t * dy
        return sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2)

    def col_f(self, m1, v1, m2, v2):  # 1_d collision formula
        v1f = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
        v2f = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
        return [v1f, v2f]

    def ref_f(self, obj, wall):
        vx = obj.vx;vy = obj.vy
        x1 = wall.x1;x2 = wall.x2
        y1 = wall.y1;y2 = wall.y2
        new_angle = (2 * atan2((y2 - y1), (x2 - x1)) - atan2(vy, vx))
        v = sqrt(vx * vx + vy * vy)
        return [v * cos(new_angle), v * sin(new_angle)]

    def collision_check(self):
        for i in range(len(self.objects)):
            obj1 = self.objects[i]
            for j in range(i + 1, len(self.objects)):
                obj2 = self.objects[j]
                if (self.distance1(obj1.px, obj1.py, obj2.px, obj2.py) <= obj1.pr + obj2.pr):
                    if (self.relations[obj1, obj2] == True):
                        continue
                    obj1.vx, obj2.vx = self.col_f(obj1.m, obj1.vx, obj2.m, obj2.vx)
                    obj1.vy, obj2.vy = self.col_f(obj1.m, obj1.vy, obj2.m, obj2.vy)
                    self.relations[obj1, obj2] = True
                    self.collisions.append([self.t, (i, j)])
                else:
                    self.relations[obj1, obj2] = False
            for k in range(len(self.walls)):
                obj2 = self.walls[k]
                if (self.distance2(obj2, obj1) <= obj2.pr + obj1.pr):
                    if (self.relations[obj1, obj2] == True):
                        continue
                    obj1.vx, obj1.vy = self.ref_f(obj1, obj2)
                    self.relations[obj1, obj2] = True
                    self.pumbs.append([self.t, (i, k)])
                else:
                    self.relations[obj1, obj2] = False


    def print_stats(self):
        s = ""
        s += (f"{self.t:0.3f}sec:\n\n")
        for i in range(len(self.objects)):
            s += (f"object{i}:\n")
            s += self.objects[i].stats() + "\n"
        s += ("\n\n")
        print(s)
