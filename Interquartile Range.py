from statistics import median
num=int(input())
X=[int(x )for x in input().split()]
Y=[int(y) for y in input().split()]
XY=sorted([])
n=sum(Y)
for i in range(n):
    XY+=[X[i]]*Y[i]
if n%2 !=0:
    q1 = median(XY[:n//2])
    q3 = median(XY[(n//2)+1:])
else:
    q1 = median(XY[:n//2])
    q2 = median(XY[n//2:])
    
print(round((q3-q1),1))

