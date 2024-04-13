from bisect import bisect_left, bisect_right

def main():
    primes = []
    primes_set = set()
    is_prime = [True]*(10**5+1)
    for i in range(2, 10**5+1):
        if not is_prime[i]:
            continue
        for j in range(2*i, 10**5, i):
            is_prime[j] = False
        primes.append(i)
        primes_set.add(i)

    valid_primes = []
    for prime in primes:
        if prime*2-1 in primes_set:
            valid_primes.append(prime*2-1)
    
    errprint(valid_primes[:10])
    Q = ini()
    for _ in range(Q):
        l, r = mapint()
        lindex = bisect_left(valid_primes, l)
        if lindex < 0 or lindex >= len(valid_primes):
            print(0)
            continue
        errprint("l,r:",l,r)
        errprint("lindex:", lindex, "v:", valid_primes[lindex])
        rindex = bisect_right(valid_primes, r)
        if rindex > len(valid_primes):
            continue
        print(rindex - lindex)
    
        
        
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