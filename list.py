a=[1,1,2,3,5,4,2,1,67,89,954,34,21]
b=[1,2,3,4,33,21,44,21,34,570,32,1001,1050,231,12]
c=[]
a1=len(a)
b1=len(b)
if a1<b1:
    print("a")
    for i in range(a1):
      if a[i] in b:
          if a[i] not in c:
              c.append(a[i])
else:
    print("b")
    for i in range(b1):
        if b[i] in a:
            if b[i] not in c:
                c.append(b[i])
print(c)
