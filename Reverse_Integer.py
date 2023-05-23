a=int(input())
if a<0:
    a=-a
    b=str(a)
    print(-1*(int(b[::-1])))
else:
    b=str(a)
    print(int(b[::-1]))