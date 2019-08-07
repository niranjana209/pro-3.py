aru=int(input())
bun=[int(i) for i in input().split()]
manj=0
for k in range(aru):
   for j in range(k):
      if bun[j]<bun[k]:
         manj+=bun[j]
print(manj) 
