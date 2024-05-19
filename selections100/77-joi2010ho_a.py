def main():
    n, m = mapint()
    
    ports = [0]*(n)
    for i in range(1,n):
        ports[i] = ini() + ports[i-1]
    
    mod = 10**5
    
    ans = 0
    curr = 0
    for i in range(m):
        d = ini()
        curr_port = ports[curr]
        next_port = ports[curr+d]
        ans += abs(next_port-curr_port)
        ans %= mod
        curr = curr+d
    print(ans % mod)
        
        
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