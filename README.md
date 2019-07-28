
ni,ar=input().split()
y=niars(leng(ar)-leng(ni))
for i in range(leng(ni)):
    if(leng(ar)==1 and ar[i] in ni):
        break
    if (ni[i]!=ar[i]):
        z=z+1
print(z)
