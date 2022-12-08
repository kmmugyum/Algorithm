from collections import deque
import sys

MAX = 100000
input = sys.stdin.readline

cur, targ = map(int, input().split())

que = deque([(cur, 0)])
visited = [0] * (MAX + 1)

min_time, ans = sys.maxsize, 0

while que:
    nx, cnt = que.popleft()
    visited[nx] = 1

    if min_time < cnt:
        break

    if nx == targ:
        min_time = cnt
        ans += 1
        continue

    if nx + 1 <= MAX and not visited[nx + 1]:
        que.append((nx + 1, cnt + 1))
    if nx - 1 >= 0 and not visited[nx - 1]:
        que.append((nx - 1, cnt + 1))
    if nx * 2 <= MAX and not visited[nx * 2]:
        que.append((nx * 2, cnt + 1))

print(min_time)
print(ans)