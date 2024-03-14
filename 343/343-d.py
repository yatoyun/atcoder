import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n, t = map(int, input().split())
    
    score_set = set()
    score_set.add(0)
    score_list = [0]*n
    score_set_dict = defaultdict(int)
    score_set_dict[0] = n
    for i in range(t):
        a, b = map(int, input().split())
        current_score = score_list[a-1]
        score_list[a-1] = current_score + b
        score_set.add(current_score + b)
        if score_set_dict[current_score] > 1:
            score_set_dict[current_score] -= 1
        else:
            score_set.remove(current_score)
            score_set_dict.pop(current_score)
        score_set_dict[current_score + b] += 1
        print(len(score_set))
    

if __name__ == "__main__":
    main()
