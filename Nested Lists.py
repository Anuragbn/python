n=[]
s=[]
N = 0
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())

    n.append(name)
    s.append(score)

    N=N+1
s1=[]
for i in range(0,N):
    s1.append(s[i])
l1=s[0]

for i in range(N):
    if l1 > s[i]:
        l1=s[i]
s.sort()

l2=s[0]
for i in range(0,N):
    if(s[i-1]==l1):
        l2=s[i]

f=[]
for i in range(0,N):
    if l2 == s1[i]:
        f.append(n[i])

f.sort()

for i in f:
    print i
