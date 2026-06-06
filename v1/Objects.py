
class Object():
  def __init__(self,p,m,v,_type="default"):
    self.p=p
    self.m=m
    self.v=v
    self._type=_type
    
  def move(self,t):
    self.p += self.v * t
  
  def stats(self):
    return(f"{self.p:0.3f} {self.m:0.3f} {self.v:0.3f}\n")
  
class Wall(Object):
  def __init__(self,p):
    from math import inf
    super().__init__(p,inf,0,"wall")

