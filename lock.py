x = [1,1,1]
y = [1,1,1]
r=0
i=0
while i<3:
    z=abs(x[i]-y[i])
    if (z<5):
        r=r+z
    else:
        r=r+(10-z)
    i=i+1
print(r)

