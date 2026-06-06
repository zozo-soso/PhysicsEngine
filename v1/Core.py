import Extras
class System():
    from math import inf
    stop = False
    pause = False
    objects = []
    relations = {}
    collisions=[]
    pr=0.35    #prescision of collision
    #collision_time=[]       i will not use right now instead
    #co_t=1
    t = 0

    def __init__(self, duration, fps, length):
        self.duration = duration
        self.fps = fps
        self.length = length

    def update(self):
      self.t+=self.fps
      self.collision_check()

    def is_running(self):
        return (not self.stop) and (self.t < self.duration)   #including updating

    def add_object(self, _object):
        for i in self.objects:
            self.relations[i, _object] = False
        self.objects.append(_object)

    def collision_check(self):
        for i in range(len(self.objects)):
            x = self.objects[i]
            if(abs(self.length-x.p)<=self.pr or x.p<=self.pr):
              x.v=-x.v
              self.collisions.append([(i),Extras.d_n(self.t,3)])
            for j in range(i + 1, len(self.objects)):
                y = self.objects[j]
                if abs(x.p - y.p) < self.pr and self.relations[x, y] == False:
                    self.relations[x, y] = True
                    if(x._type!="wall" and y._type!="wall"):
                      v2f = ((y.m - x.m) * y.v + 2 * x.m * x.v) / (x.m + y.m)
                      v1f = ((x.m - y.m) * x.v + 2 * y.m * y.v) / (x.m + y.m)
                      x.v = v1f
                      y.v = v2f
                    elif x._type=="wall":
                      y.v=-y.v
                    elif y._type=="wall":
                      x.v=-x.v
                    self.collisions.append([(i,j),Extras.d_n(self.t,3)])
                else:
                    if abs(x.p - y.p) > self.pr:
                      self.relations[x, y] = False

    def print_stats(self):
      s=""
      s+=(f"{self.t:0.3f}sec:\n\n")
      for i in range(len(self.objects)):
        s+=(f"object{i}:\n")
        s+=self.objects[i].stats()+"\n"
      s+=("\n\n")
      print(s)
