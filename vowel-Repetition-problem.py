s=input()
v="aeiou"
d={}
mx=0
for i in s:
     if i in v:
          d[i]+=1
     else:
         d[i]=1
     if d[i]>mx:
         mx=d[i]
         ans=i
print(ans)
