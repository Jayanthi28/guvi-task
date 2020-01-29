a=int(input("enter the number:"))
f=0
s=1
if(a<=0):
    print("the requested series",f)
else:
     print(f,s,end="")
     for i in range(2,a):
      next=f+s
      print(next,end="")
      f=s
      s=next
