from collections import defaultdict

def main():
    N = ini()
    Q = ini()
    
    card_dict = defaultdict(set)
    box_dict = defaultdict(list)
    
    for i in range(Q):
        query = lint()
        if query[0] == 1:
            box_dict[query[2]].append(query[1])
            card_dict[query[1]].add(query[2])
        elif query[0] == 2:
            cards = box_dict[query[1]]
            print(*sorted(cards))
        else:
            boxes = card_dict[query[1]]
            print(*sorted(list(boxes)))

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
