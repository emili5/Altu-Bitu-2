
from collections import deque

deq = deque()
n = int(input())
order = list(map(int,input().split()))
order[::] = order[::-1]

for i in range(n):
    if order[i]==1:
        deq.appendleft(i+1)
    elif order[i]==2:
        x = deq.popleft()
        deq.appendleft(i+1)
        deq.appendleft(x)
    else:
        deq.append(i+1)
for i in deq:
    print(i,end=" ")