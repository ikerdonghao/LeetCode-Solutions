class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def is_greater_than_radius(x1,x2,y1,y2,radius):
            return (x1-x2) ** 2 + (y1-y2) ** 2 > radius ** 2
        if yCenter > y2+radius or yCenter < y1-radius or xCenter > x2+radius or xCenter < x1-radius:
            print("Check option 1")
            return False
        elif (xCenter >= x1 and xCenter <= x2) or (yCenter >= y1 and yCenter <= y2):
            print("Check option 2")
            return True
        elif is_greater_than_radius(xCenter,x1,yCenter,y1,radius) and is_greater_than_radius(xCenter,x1,yCenter,y2,radius) and is_greater_than_radius(xCenter,x2,yCenter,y1,radius) and is_greater_than_radius(xCenter,x2,yCenter,y2,radius):
            print("Check option 3")
            return False
        else:
            print("Check option 4")
            return True