class Point:
    def __init__(self, xinit, yinit):
        self.x = xinit
        self.y = yinit

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distfromorigin(self):
        return ((self.x**2) + (self.y**2))**.5

    def distfrompoint(self, target):
        return(((self.x - target.x)**2) + ((self.y - target.y)**2))**.5

    def translate(self, xtrans, ytrans):
        newx = self.x + xtrans
        newy = self.y + ytrans
        return newx, newy


def distbetweenpoints(point1, point2):
    return(((point1.x - point2.x)**2) + (point1.y - point2.y)**2)**.5

p = Point(7, 6)
q = Point(-3, 5)
p.getx()
p.distfrompoint(q)
distbetweenpoints(p, q)
p.translate(-2, 7)
q.translate(-7, 2)
print("The point p is", p)
print("The point q is", q)
print(distbetweenpoints(p, q))
