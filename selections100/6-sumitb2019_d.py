import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline

def main():
    N = int(input())
    S = input().strip()
        
    indices_list = [[] for _ in range(10)]
    for i, s in enumerate(map(int, S)):
        indices_list[s].append(i)
    last_indices = []
    for indices in indices_list:
        last_indices.append(indices[-1] if indices else -1)

    ans = 0
    for i in range(10):
        index_0 = indices_list[i][0] if indices_list[i] else -1
        if index_0 == -1:
            continue
        for j in range(10):
            vi = bisect_right(indices_list[j], index_0)
            index_1 = indices_list[j][vi] if vi < len(indices_list[j]) else -1
                
            if index_1 == -1 or index_0 >= index_1:
                continue
            
            for k in range(10):
                index_2 = last_indices[k]
                if index_2 != -1 and index_1 < index_2:
                    ans += 1
            
    print(ans)
    
    

if __name__ == "__main__":
    main()