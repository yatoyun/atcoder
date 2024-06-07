from bisect import bisect_left, bisect_right

def main():
    N, P, Q, R = mapint()
    A = lint()
    
    sums = [A[0]]
    for i in range(1, N):
        sums.append(sums[-1] + A[i])
        
    P_list = []
    left = 0
    curr = 0
    right = 0
    while right < N:
        if curr == P:
            P_list.append(right)
            curr += A[right]
            right += 1
        if curr < P:
            curr += A[right]
            right += 1
        else:
            curr -= A[left]
            left += 1
    
    Q_list = []
    for left in P_list:
        curr = 0
        index = bisect_left(sums, sums[left-1] + Q)
        if index >= N:
            continue
        if sums[index] == sums[left-1] + Q:
            Q_list.append(index+1)
    
    
    for left in Q_list:
        curr = 0
        index = bisect_left(sums, sums[left-1] + R)
        if index >= N:
            continue
        if sums[index] == sums[left-1] + R:
            print("Yes")
            return
    print("No")

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