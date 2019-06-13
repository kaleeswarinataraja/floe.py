a1,a2=map(int,input().split())
s=a1+1
for i in range(s,a2):
  if i%2!=0:
    print(i,end=" ")
