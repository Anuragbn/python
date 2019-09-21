# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
x=OrderedDict()
n=int(raw_input())
for i in range(n):
    k,v=raw_input().rsplit(' ',1)
    if k in x.keys():
        a=str(int(x[k])+int(v))
        x.update({k:a})    
    else:
        x.update({k:v})

for k,v in x.items():
    print k,v
