#FIrst TRY
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



###########################################################################
#SEcond TRY


import statistics as st

n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()

if n%2 != 0:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2+1:])
else:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2:])

ir = round(float(q3-q1), 1)
print(ir)
