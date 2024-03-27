import sys
from collections import deque
import heapq
input = sys.stdin.readline

def main():
    N = int(input())
    
    S = []
    cnt_dict = {}
    for _ in range(N):
        s, c = input().split()
        S.append(int(s))
        cnt_dict[int(s)] = int(c)
    
    S.sort()
    que = deque()
    
    for s in S:
        cnt = cnt_dict[s] // 2
        cnt_dict[s] -= cnt*2
        if s*2 not in cnt_dict:
            cnt_dict[s*2] = 0
            que.append(s*2)
        cnt_dict[s*2] += cnt

    while que:
        s = que.popleft()
        cnt = cnt_dict[s] // 2
        if cnt == 0:
            continue
        cnt_dict[s] -= cnt*2
        que.append(s*2)
        if s*2 not in cnt_dict:
            cnt_dict[s*2] = 0
        cnt_dict[s*2] += cnt    

    print(sum(cnt_dict.values()))

if __name__ == "__main__":
    main()