from math import sin,cos
class Object():
  def __init__(self,px,py,m,v,angle,_type="default"):

    self.px=px
    self.py=py
    self.m=m
    self.vx=v*cos(angle)
    self.vy=v*sin(angle)
    self._type=_type

  def move(self,t):
    self.px += self.vx * t
    self.py += self.vy * t
  
  def stats(self):
    return(f"({self.px:0.3f},{self.py:0.3f}) {self.m:0.3f} ({self.v:0.3f},{self.angle:0.1f}')\n")
  
class Wall(Object):
  def __init__(self,px,py):
    from math import inf
    super().__init__(px,py,inf,0,0,"wall")

