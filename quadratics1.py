 import math
def qsolve(a,b,c):
    d=b*b-4*a*
    if d<0:
        print("can't solve")
    elif d==0:
        x = -b/(2*a)
        print("x =", round(x,1))
    else:
        rootd = math.sqrt(d)
        x1 = (-b + rootd) / (2*a)
        x2 = (-b - rootd) / (2*a)
        print("x =",round(x1,1),"x =",round(x2,1))

