import Core,Objects,Extras
import matplotlib.pyplot as plt
import time

s1=Core.System(30,0.1,100)
s1.pr=1
s1.add_object(Objects.Object(4,1,0))
s1.add_object(Objects.Object(8,1000,-1.0))
#s1.add_object(Objects.Wall(3))
plt.ion()
fig,ax=plt.subplots()

points =[]
for i in s1.objects:
  point, =ax.plot([],[],'o')
  points.append(point)
ax.set_xlim(-1,1)
ax.set_ylim(0,s1.length)
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
    points[i].set_data([0], [obj.p])
  plt.draw()
  plt.pause(max(s1.fps-dt,0.01))
print(len(s1.collisions))
