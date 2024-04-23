from collections import defaultdict
def main():
    N = ini()
    N -= 1
    num = len(format(N, "b"))
    people = defaultdict(list)
    print(num)
    sys.stdout.flush()
    for bit in range(1 << num):
        if bit > N:
            break
        for j in range(num):
            if bit & (1 << j):
                people[j+1].append(bit)
    errprint(people)
    for i, v in people.items():
        print(len(v), *v)
        sys.stdout.flush()
    S = input().rstrip()
    ans = int(S[::-1], 2)
    if ans == 0:
        ans = N + 1
    print(ans)
    sys.stdout.flush()

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
