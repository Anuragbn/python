if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

f=arr[0]

for i in range(0,n):
    if f<arr[i]:
        f=arr[i]

arr.sort()
for i in range(0,n):
    if(f!=arr[i]):
        s=arr[i]

print s
