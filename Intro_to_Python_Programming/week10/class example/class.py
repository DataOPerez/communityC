class Point(): # heading for a class called point

    numPoint = 0 # this is a static attriubte, everyone has access to that.

    def __init__(self, x, y): # this is still a function and all the rules of function apply.
        '''Constructor - initialize the attributes of an object'''
        print("Constructing a Point Object.")
        # each object get's it's own copy
        self.x = x # object attribute
        self.y = y # object attribute
        Point.numPoint += 1 # accessing the static attribute numPoints

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def translatePoint(self, dx, dy):
        '''shift the point in the x direct by dx and y direction by dy'''
        self.x += dx
        self.y += dy

    def getDistance(self, otherPoint):
        '''return a float representing the distance between two points'''
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y
        return (dx**2 + dy**2) ** 0.5

    @staticmethod
    def getMidPoint(point1, point2):
        '''find a return a point object that is the midpoint of the arguemnts'''
        newX = (point1.x + point2.x) / 2
        newY = (point1.y + point2.y) / 2
        return Point(newX, newY)



def main():
    p1 = Point(2, 3) # p1 is an instance of Point
    p2 = Point(4, 5)

    midPoint = Point.getMidPoint(p1, p2)

    print(p1)
    print(p2)
    print(midPoint)

    p1.translatePoint(6, 7)
    print('after translating')
    print(p1)
    print(p2)

    print("distance between p1 and p2")
    dist = p1.getDistance(p2)
    print(dist)
if __name__ == '__main__':
    main()