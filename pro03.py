niran,arr=input().split()
pan=abs(len(niran)-len(arr))
for i in range(len(niran)):
  if len(arr)==1 and arr[i] in niran:
   break
  if niran[i]!=arr[i]:
   pan+=1
print(pan)
