import sys
from collections import deque

input = sys.stdin.readline

MAX = 100000
current, target = map(int, input().split())

visited = [0] * (MAX + 1)

que = deque([(current, 0)])
shortest, methods = sys.maxsize, 0

while que:
    cur, cnt = que.popleft()
    visited[cur] = 1

    if cnt > shortest:
        break

    if cur == target:
        shortest = cnt
        methods += 1
        continue

    if cur + 1 <= MAX and not visited[cur + 1]:
        que.append((cur + 1, cnt + 1))
    if cur - 1 >= 1 and not visited[cur - 1]:
        que.append((cur - 1, cnt + 1))
    if cur * 2 <= MAX and not visited[cur * 2]:
        que.append((cur * 2, cnt + 1))

print(shortest)
print(methods)