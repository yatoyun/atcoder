import sys
from collections import defaultdict
input = sys.stdin.readline

def select(num_dict, i, j, current, M):
    max_num = 1000
    index = -1
    current_index = (current) % M

    for num in num_dict[i][j]:
        if num < 0:
            continue
        if num < current_index and (M-current_index)+num < max_num:
            max_num = (M-current_index)+num
            index = i
        elif num >= current_index and num-current_index < max_num:
            max_num = num-current_index
            index = i
    
    return index, max_num
        
        

def main():
    M = int(input())
    S = [list(map(int, list(input().rstrip()))) for _ in range(3)]

    num_dict = [defaultdict(list) for _ in range(3)]
    for i in range(3):
        for j in range(M):
            num_dict[i][S[i][j]].append(j)
        for j in range(10):
            num_dict[i][j].append(-1)
    ans = 10**9
    for i in range(10):
        flag = True
        for j_list in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]:
            total_time = 0
            for j in j_list:
                index, time = select(num_dict, j, i, total_time, M)
                if index == -1:
                    flag = False
                    break
                total_time += time
                if j != j_list[-1]:
                    total_time += 1
            if not flag:
                break
            if flag:
                ans = min(total_time, ans)
    print(ans if ans != 10**9 else -1)
            

if __name__ == "__main__":
    main()