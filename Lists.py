if __name__ == '__main__':
    N = int(raw_input())
l = []
for n in range(N):
    x = raw_input().split(" ")
    a = x[0]
    if a == 'append':
        l.append(int(x[1]))
    if a == 'print':
        print l
    if a == 'insert':
        l.insert(int(x[1]), int(x[2]))
    if a == 'reverse':
        l.reverse()
    if a == 'pop':
        l.pop()
    if a == 'sort':
        l.sort()
    if a == 'remove':
        l.remove(int(x[1]))

