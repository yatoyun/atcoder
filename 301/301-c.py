import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    S = input().rstrip()
    T = input().rstrip()
    
    chargeable_set = set(["a", "t", "c", "o", "d", "e", "r"])
    
    al_dict = defaultdict(int)
    s_at = 0
    t_at = 0
    
    for s, t in zip(S, T):
        if s == "@":
            s_at += 1
        else:
            al_dict[s] += 1
            
        if t == "@":
            t_at += 1
        else:
            al_dict[t] -= 1
    
    for al, cnt in al_dict.items():
        if cnt == 0:
            continue
        
        if al not in chargeable_set:
            print("No")
            return
        if cnt > 0:
            t_at -= cnt
        else:
            s_at -= cnt
        
        if s_at < 0 or t_at < 0:
            print("No")
            return
    print("Yes")
    
    




if __name__ == '__main__':
    main()


