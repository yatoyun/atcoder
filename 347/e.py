from collections import defaultdict
def main():
    N, Q = mapint()
    X = lint()
    
    nums_indexes = defaultdict(list)
    num_set = set()
    sum_nums = [0]
    for i in range(Q):
        x = X[i]
        if x not in num_set:
            num_set.add(x)
        else:
            num_set.remove(x)
        nums_indexes[x].append(i)
        sum_nums.append(sum_nums[-1] + len(num_set))
    errprint(nums_indexes)
    errprint(sum_nums)
    for n in range(1, N+1):
        if n not in nums_indexes:
            print(0, end = " ")
            continue
        
        indexes = nums_indexes[n]
        if len(indexes) % 2 == 1:
            indexes.append(Q)
        cnt = 0
        errprint(n)
        for i in range(0, len(indexes), 2):
            l = indexes[i]
            r = indexes[i+1]
            cnt += sum_nums[r] - sum_nums[l]
            errprint(sum_nums[r], sum_nums[l])
        print(cnt, end = " ")
    

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