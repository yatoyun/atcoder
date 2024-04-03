from bisect import bisect_left, bisect_right
def main():
    N = ini()
    A = lint()
    Q = ini()
    
    sleep_st = []
    sleep_ed = []
    sleep_sum = [A[0]]
    for i in range(1,N):
        if i % 2 == 1:
            sleep_st.append(A[i])
        else:
            sleep_ed.append(A[i])
            
            sleep_sum.append(sleep_sum[-1] + (sleep_ed[-1] - sleep_st[-1]))
    errprint(sleep_st)
    errprint(sleep_ed)
    errprint(sleep_sum)
    for _ in range(Q):
        l, r = mapint()
        
        ans = 0
        # st
        first_sleep_st = bisect_left(sleep_st, l)
        if first_sleep_st > 0 and sleep_ed[first_sleep_st-1] > l:
            ans += sleep_ed[first_sleep_st-1] - l
            if sleep_ed[first_sleep_st-1] > r:
                print(r-l)
                continue
        if sleep_st[first_sleep_st] > r:
            print(ans)
            continue

        # ed
        last_sleep_st = bisect_right(sleep_st, r)-1
        
        if sleep_ed[last_sleep_st] > r:
            ans += r - sleep_st[last_sleep_st]
            last_sleep_ed = last_sleep_st - 1
        else:
            last_sleep_ed = last_sleep_st
        errprint(ans)
        # sum
        ans += sleep_sum[last_sleep_ed+1] - (sleep_sum[first_sleep_st])
        print(ans)

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