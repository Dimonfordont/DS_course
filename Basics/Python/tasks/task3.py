import sys
import os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def main():
    n, k = map(int, input().split())

    safe = [False] * (n + 1)
    safe[0] = True
    safe[n] = True

    if k > 0:
        platforms = list(map(int, input().split()))
        for p in platforms:
            safe[p] = True

    INF = float('inf')
    dp = [INF] * (n + 1)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        if not safe[i]:
            continue
        if i + 1 <= n and safe[i + 1]:
            dp[i] = min(dp[i], dp[i + 1] + 1)
        if i + 2 <= n and safe[i + 2]:
            dp[i] = min(dp[i], dp[i + 2] + 1)

    if dp[0] == INF:
        print(-1)
        return
    print(dp[0])
    path = []
    pos = 0
    while pos < n:
        if pos + 1 <= n and safe[pos + 1] and dp[pos + 1] == dp[pos] - 1:
            path.append('1')
            pos += 1
        else:
            path.append('2')
            pos += 2
    print(''.join(path))
main()
