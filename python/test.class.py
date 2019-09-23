import math

class Point:

 def __init__(self,x,y):
  self.x = x
  self.y = y

 def get_distance(self,p):
  return math.sqrt((self.x-p.x)**2 + (self.y - p.y)**2)

# def get_midpoint(self,p):
#  return Point((self.x + p.x)/ 2, (self.y + p.y)/ 2))
#  pass

p1 = Point(5,7)

p2 = Point(2,3)

print(p1.get_distance(p2))

#mp = p1.get_midpoint(p2)

#print(str(mp.x) + ',' + str(mp,y))
