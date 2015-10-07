class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getDistanceFromOrigin(self):
        return ((self.x**2)+(self.y**2))**.5
    def getDistanceFromPoint(self, p):
        self.point = p
        return (((self.x-self.point.getX())**2)+((self.y-self.point.getY())**2))**.5
    def translate(self, x, y):
        #pick how much to increase/decrease x or y
        self.x += x
        self.y += y
    def getSlope(self):
        #return the slope
        return (self.getY())/(self.getX())
    def cleanSlate(self):
        #set point to equal origin
        self.x = 0
        self.y = 0
    def reflectAcrossAxis(self, axis):
        if(axis == "x") or (axis == "X"):
                self.translate(-(self.getX()*2),0)
        if(axis == "y") or (axis == "Y"):
                self.translate(0,-(self.getY()*2))
def getDistanceBetweenPoints(self, x, y):
    return (((self.x-x)**2)+((self.y-y)**2))**.5
p = point(5,3)
q = point(5,4)
print("The Point p lies on (" + str(p.getX()) + ", " + str(p.getY())+ ")")
print("The Point q lies on (" + str(q.getX()) + ", " + str(q.getY())+ ")")
print("The Point's distance from the origin is " + str(p.getDistanceFromOrigin()) + " units")
print("The Point's distance from Point q is " + str(p.getDistanceFromPoint(q)) + " units")
p.reflectAcrossAxis("x")
print("The Point p reflected across the X axis is (" + str(p.getX()) + ", " + str(p.getY())+ ")")
p.reflectAcrossAxis("x")
p.reflectAcrossAxis("y")
print("The Point p reflected across the Y axis is (" + str(p.getX()) + ", " + str(p.getY())+ ")")