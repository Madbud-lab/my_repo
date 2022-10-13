x = list(map(int,input().split()))
while(x[1]!=0):
    r = x[0] % x[1]
    x[0] = x[1]
    x[1] = r
print(x[0])
