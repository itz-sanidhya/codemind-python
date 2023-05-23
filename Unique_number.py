n=int(input())
temp=n
l=[]
while temp!=0:
    a=temp%10
    l.append(a)
    temp=temp//10
s=set(l)
if len(l)==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")
