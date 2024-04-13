def main():
    S = lstr()
    al_dict  = {}
    for s in S:
        if s in al_dict:
            al_dict[s] += 1
        else:
            al_dict[s] = 1
    
    errprint(al_dict)
    i_dict = {}
    for i, v in al_dict.items():
        if v in i_dict:
            i_dict[v] += 1
        else:
            i_dict[v] = 1
    errprint(i_dict)
    for i in i_dict.values():
        if i == 0 or i == 2:
            continue
        else:
            print("No")
            return
    print("Yes")

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