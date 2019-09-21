from collections import defaultdict
x=defaultdict(list)

n,m=map(int,raw_input().split(' '))

for i in range(n):
    x[raw_input()].append(i+1)

l=[]
for i in range(m):
    l.append(raw_input())


for i in l:
    print(' '.join(map(str,x[i])) or -1)
    
