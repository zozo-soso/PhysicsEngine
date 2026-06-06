import Core,Objects,Extras
import matplotlib.pyplot as plt
import time

s1=Core.System(60,0.1,8,8)
s1.pr=1
s1.add_object(Objects.Object(1.2,3,2,5,15))
s1.add_object(Objects.Object(5,5,4,3,70))
s1.add_object(Objects.Object(3,6,5,4,0))
s1.add_object(Objects.Object(2,5,3,8,5))
s1.add_object(Objects.Wall(5,4))
plt.ion()
fig,ax=plt.subplots()

points =[]
for i in s1.objects:
  point, =ax.plot([],[],'o',markersize=s1.pr*20)
  points.append(point)
ax.set_xlim(-s1.pr,s1.lengthx+s1.pr)
ax.set_ylim(-s1.pr,s1.lengthy+s1.pr)
plt.show()
last=time.time()
while(s1.is_running()):
  now=time.time()
  dt=now-last
  last=now
  s1.update()
  p=[]
  for i, obj in enumerate(s1.objects):
    obj.move(s1.fps)
    points[i].set_data([obj.px], [obj.py])
  plt.draw()
  plt.pause(max(s1.fps-dt,0.01))
print(len(s1.collisions)+len(s1.pumbs))
