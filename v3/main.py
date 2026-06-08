import Core,Objects,graph
import time

lx,ly=25,30
duration=10
fps=15
s1=Core.System(duration,fps,lx,ly)
g1=graph.Graph(lx,ly)


s1.add_object(Objects.Object(6,7,5,18,90))
s1.add_object(Objects.Object(7,5,12,14,80,0.8))
s1.add_object(Objects.Object(10,6,10,15,0,0.7))
s1.add_object(Objects.Object(4,9,20,10,45,1))
s1.add_object(Objects.Object(2.5,ly-5,1,2,0,1))
s1.add_wall(Objects.Wall(0,ly-10,lx,ly-10,1))
s1.add_wall(Objects.Wall(9,15,4,9,0.7))
s1.add_wall(Objects.Wall(13,12,8,8,1.2))
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
