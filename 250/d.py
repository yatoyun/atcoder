def main():
    N = ini()

    primes = [True]*(int(pow(N,1/3))+1)
    for i in range(int(pow(N,1/3))+1):
        if i < 2:
            primes[i] = False
            continue

        if not primes:
            continue
        for j in range(i*2, int(pow(N,1/3))+1, i):
            primes[j] = False
    
    nums_primes = [0]*(int(pow(N,1/3))+1)
    for i in range(1, int(pow(N,1/3))+1):
        if primes[i]:
            nums_primes[i] = 1
        nums_primes[i] += nums_primes[i-1]

    cnt = 0
    for q in range(2, int(pow(N,1/3))+1):
        if primes[q]:
            max_p = N // pow(q, 3)
            max_p = min(max_p, q-1)
            errprint(q, max_p)
            cnt += nums_primes[max_p]
    print(cnt)


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