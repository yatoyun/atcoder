from bisect import bisect_left, bisect_right

def calc(a, b, c):
    return (a**2)*b*(c**2)

def main():
    N = ini()
    is_prime = [True]*(4*(10**5))
    prime_nums = [2]
    prime_nums2 = [4]
    
    for i in range(3, 4*(10**5), 2):
        if not is_prime[i]:
            continue
        
        prime_nums.append(i)
        prime_nums2.append(i**2)
        temp = i*2
        while temp < 4*(10**5):
            is_prime[temp] = False
            temp += i

    count = 0
    M = len(prime_nums)
    for i in range(M-2):
        a = prime_nums[i]
        if a**5 > N:
            break
        j = i + 1
        while j < M-1:
            b = prime_nums[j]
            if (a**2)*(b**3) > N:
                break
            k = bisect_right(prime_nums2, N//((a**2)*b))-1
            c = prime_nums[k]
            if k <= j:
                break
            count += k - j
            j += 1        
    print(count)
        

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
