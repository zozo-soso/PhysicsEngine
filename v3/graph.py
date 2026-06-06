import matplotlib.pyplot as plt
class Graph():
    fig,ax=plt.subplots()
    points={}           #obj:[x_cord,y_cord,radius]
    lines={}            #wall:[x1_cord,y1_cord,x2_cord,y2_cord,width]
    def __init__(self,lenx,leny):
        self.lengthx=lenx
        self.lengthy=leny
        self.ax.set_xlim(-0.05 * self.lengthx, 1.05 * self.lengthx)
        self.ax.set_ylim(-0.05 * self.lengthy, 1.05 * self.lengthy)

    def add_point(self,obj):
        self.points[obj] = plt.Circle((obj.px,obj.py),obj.pr)
    def add_line(self,wall):
        line, = self.ax.plot([wall.x1, wall.x2], [wall.y1, wall.y2],linewidth= wall.pr*10)
        self.lines[wall]=line
    def run(self):
        plt.ion()
        for p in self.points:
            self.ax.add_patch(self.points[p])
        plt.show()
    def update(self,objs):
        for obj in objs:
            self.points[obj].set_center((obj.px,obj.py))
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
    def _pause(self,t):
        plt.pause(t)