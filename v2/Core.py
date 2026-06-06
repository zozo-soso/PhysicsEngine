import Extras
from math import inf, sin, cos
class System():

    stop = False
    pause = False
    objects = []
    relations = {}
    collisions=[]
    pumbs=[]
    pr=0.35    #prescision of collision
    #collision_time=[]       i will not use right now instead
    #co_t=1
    t = 0

    def __init__(self, duration, fps, lengthx,lengthy):

        self.duration = duration
        self.fps = fps
        self.lengthx = lengthx
        self.lengthy = lengthy

    def update(self):
      self.t+=self.fps
      self.collision_check()

    def is_running(self):
        return (not self.stop) and (self.t < self.duration)   #including updating

    def add_object(self, _object):
        for i in self.objects:
            self.relations[i, _object] = False
        self.objects.append(_object)

    def distance(self,ob1,ob2):
        return(pow(pow(ob1.px-ob2.px,2)+pow(ob1.py-ob2.py,2),0.5))

    def col_f(self,m1,v1,m2,v2):        #1_d collision formula
        v1f = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
        v2f = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
        return [v1f,v2f]

    def collision_check(self):
        for i in range(len(self.objects)):
            x = self.objects[i]
            if(x.px>self.lengthx):
              x.vx*=-1
              x.px=self.lengthx
            elif(x.px<0):
                x.vx*=-1
                x.px=0
                self.pumbs.append([(i),Extras.d_n(self.t,3)])
            if(x.py>self.lengthy):
              x.vy*=-1
              x.py=self.lengthy
            elif(x.py<0):
                x.vy*=-1
                x.py=0
                self.pumbs.append([(i), Extras.d_n(self.t, 3)])
            for j in range(i + 1, len(self.objects)):
                y = self.objects[j]
                if self.distance(x,y)<=self.pr and self.relations[x, y] == False:
                    self.relations[x, y] = True
                    if(x._type!="wall" and y._type!="wall"):
                      lstx=self.col_f(x.m,x.vx,y.m,y.vx)
                      x.vx=lstx[0]
                      y.vx=lstx[1]
                      lsty = self.col_f(x.m, x.vy, y.m, y.vy)
                      x.vy = lsty[0]
                      y.vy = lsty[1]
                      self.collisions.append([(i, j), Extras.d_n(self.t, 3)])
                    elif x._type=="wall":
                      y.vx*=-1
                      y.vy*=-1
                      self.pumbs.append([(i, j), Extras.d_n(self.t, 3)])
                    elif y._type=="wall":
                        x.vx *= -1
                        x.vy *= -1
                        self.pumbs.append([(i, j), Extras.d_n(self.t, 3)])

                else:
                    if self.distance(x,y) > self.pr:
                      self.relations[x, y] = False

    def print_stats(self):
      s=""
      s+=(f"{self.t:0.3f}sec:\n\n")
      for i in range(len(self.objects)):
        s+=(f"object{i}:\n")
        s+=self.objects[i].stats()+"\n"
      s+=("\n\n")
      print(s)
