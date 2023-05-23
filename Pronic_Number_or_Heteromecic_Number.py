n=int(input())
c=0
for x in range(1,n):
    a=x*(x-1)
    if a==n:
        print("YES")
        c+=1
    else:
        continue
if c==0:
    print("NO")



    

    
