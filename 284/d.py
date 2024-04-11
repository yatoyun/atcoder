def main():
    prime_numbers = []
    num_list = [True] * 3*pow(10, 6)
    
    for i in range(2, 3*pow(10, 6)):
        if num_list[i]:
            prime_numbers.append(i)
            for j in range(i*2, 3*pow(10, 6), i):
                num_list[j] = False
    
    T = ini()
    for _ in range(T):
        test = ini()
        max_a = float("inf")
        for prime in prime_numbers:
            if test % prime == 0:
                max_a = prime
                break
        if test % max_a == 0:
                p = int(pow(test // max_a, 0.5))
                q = max_a
        if test % (max_a)**2 == 0:
            p = max_a
            q = test // (max_a)**2
        print(p, q)
            
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