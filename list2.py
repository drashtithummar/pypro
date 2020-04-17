a=['drashti','eklavy','rutika','sussina','ru',2,3]
a1=len(a)
c=0
for i in range(a1):
    if type(a[i]) is str:
        if len(a[i])>=2:
            c+=1
print(c)
