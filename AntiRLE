with open ('1.txt') as inf:
    s = inf.readline().strip()[::-1]
f=''
k=''
n=''
for c in s:
    if '0'<=c<='9':
        n+=c
    else:
        k=c*(int(n[::-1]))
        f +=k
        n = ''
with open('2.txt', 'w') as ouf:
    ouf.write(f[::-1])
