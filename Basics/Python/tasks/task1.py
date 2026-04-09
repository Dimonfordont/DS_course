import sys
import os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    diff = [0] * (n + 2)
    for _ in range(q):
        l, r = map(int, input().split())
        diff[l] += 1
        diff[r + 1] -= 1
    freq = [0] * (n + 1)
    cur = 0
    for i in range(1, n + 1):
        cur += diff[i]
        freq[i] = cur
    a.sort(reverse=True)
    counts = sorted(freq[1:], reverse=True)

    result = 0
    for i in range(n):
        result += a[i] * counts[i]

    print(result)

main()
