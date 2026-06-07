from math import sin, cos


class Object():
    def __init__(self, px, py, m, v, angle, pr=0.5):
        self.px = px
        self.py = py
        self.m = m
        self.vx = v * cos(angle)
        self.vy = v * sin(angle)
        self.pr = pr
        self._type = "default"

    def move(self, t):
        self.px += self.vx * t
        self.py += self.vy * t

    def stats(self):
        return (f"({self.px:0.3f},{self.py:0.3f}) {self.m:0.3f} ({self.v:0.3f},{self.angle:0.1f}')\n")


class Wall():
    def __init__(self, x1, y1, x2, y2, pr=1.5):
        from math import inf
        self.x1 = min(x1,x2)
        self.x2 = max(x1,x2)
        self.y1 = min(y1,y2)
        self.y2 = max(y1,y2)
        self.pr = pr
        self._type = "wall"
