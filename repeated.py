# repeated.py
n=int(input())
l=[]
c=[]
for i in range(n):
    l.append(input())
for o in l:
    k=l.count(o)
    if(k>1):
        if (o not in c):
            c.append(o)
print(' '.join(c))
