import Core,Objects,graph
import time

lx,ly=10,15
duration=20
fps=15
s1=Core.System(duration,fps,lx,ly)
g1=graph.Graph(lx,ly)


s1.add_object(Objects.Object(2,7,2,8,15))
s1.add_object(Objects.Object(5,5,4,4,80))
s1.add_object(Objects.Object(3,6,5,10,0))
s1.add_object(Objects.Object(3,9,20,2,180))
s1.add_wall(Objects.Wall(9,10,4,4))
s1.add_wall(Objects.Wall(13,5,8,1))
for obj in s1.objects:
  g1.add_point(obj)
for wall in s1.walls:
  g1.add_line(wall)

s1.run()
g1.run()

last=time.time()
while s1.is_running():
  if s1.pause:
    continue
  #print(s1.t)
  #now=time.time()
  #dt=now-last
  #last=now
  s1.update()
  g1.update(s1.objects)
  #g1._pause(1/s1.fps)
  #g1._pause(max(1/s1.fps - dt, 0.01))
print(str(len(s1.collisions))+" "+str(len(s1.pumbs)))
