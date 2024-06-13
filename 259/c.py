def main():
    S = lstr()
    T = lstr()

    s_index = 1
    t_index = 1
    if S[0] != T[0]:
        print("No")
        return
    flag = False
    S.append("")
    while t_index < len(T):
        if S[s_index] == T[t_index]:
            if S[s_index-1] == S[s_index]:
                flag = True
            else:
                flag = False
            s_index += 1
            t_index += 1
            if s_index > len(S):
                print("No")
                return
        elif flag and T[t_index] == T[t_index-1]:
            t_index += 1
        else:
            print("No")
            return
        # errprint("".join(S[:s_index]), "".join(T[:t_index]), s_index, t_index)
    print("Yes" if t_index == len(T) and s_index < len(S) else "No")

def ini(): return int(input())
def mapint(): return map(int, input().split())
def mapint0(): return map(lambda x: int(x)-1, input().split())
def mapstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lint0(): return list(map(lambda x: int(x)-1, input().split()))
def lstr(): return list(input().rstrip())
def errprint(*x): return None if atcenv else print(*x, file=sys.stderr) 

if __name__=="__main__":
    import sys, os
    input = sys.stdin.readline
    atcenv = os.environ.get("ATCODER", 0)
    main()