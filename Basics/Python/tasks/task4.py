
"""
imma a dumdum cladue cdoe egant howeva i too dubble as a yandex algo solva via playwright
"""

import sys
import os
from collections import deque

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    artifacts = []
    for epoch in range(n):
        values = list(map(int, input().split()))
        for v in values:
            artifacts.append((v, epoch))

    artifacts.sort()

    epoch_deques = [deque() for _ in range(n)]
    covered = 0
    left = 0
    running_sum = 0
    min_range = float('inf')
    best_sum = float('inf')
    best_left = 0
    best_right = 0

    for right in range(len(artifacts)):
        val, ep = artifacts[right]
        epoch_deques[ep].append(right)
        if len(epoch_deques[ep]) == 1:
            covered += 1
            running_sum += val

        while covered == n:
            range_val = artifacts[right][0] - artifacts[left][0]

            if range_val < min_range or (range_val == min_range and running_sum < best_sum):
                min_range = range_val
                best_sum = running_sum
                best_left = left
                best_right = right

            lep = artifacts[left][1]
            old_min_val = artifacts[epoch_deques[lep][0]][0]
            epoch_deques[lep].popleft()
            if len(epoch_deques[lep]) == 0:
                covered -= 1
                running_sum -= old_min_val
            else:
                new_min_val = artifacts[epoch_deques[lep][0]][0]
                running_sum += new_min_val - old_min_val
            left += 1

    chosen = {}
    for i in range(best_left, best_right + 1):
        val, ep = artifacts[i]
        if ep not in chosen:
            chosen[ep] = val

    result = sorted(chosen.values())
    print(' '.join(map(str, result)))
main()
