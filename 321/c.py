import sys
from collections import deque
input = sys.stdin.readline

def main():
    K = int(input())
    
    que = deque()
    que.append("")
    num_list = []
    while que:
        S = que.popleft()
        start = int(S[-1])+1 if S else 0
        for i in range(start, 10):
            new_S = S + str(i)
            num_list.append(int(new_S[::-1]))
            que.append(new_S)
    
    num_list.sort()
    print(num_list[K])
    

if __name__ == "__main__":
    main()
