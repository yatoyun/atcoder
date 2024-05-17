#####segfunc#####
def segfunc(x, y):
    if x[0] <= y[0]:
        return x
    else:
        return y
#################

#####ide_ele#####
ide_ele = 2**31-1
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def main():
    N, K = mapint()
    P = lint0()
    
    eaten_turns = [-1]*N
    eaten_cards = [[] for _ in range(N)]
    sg = SegTree([(ide_ele,-1) for _ in range(N)], segfunc, (ide_ele,-1))
    
    max_index = -1
    for i in range(N):
        p = P[i]
        min_v = sg.query(p, N)
        min_x, index = min_v
        if min_x == ide_ele:
            sg.update(p, (p, max_index+1))
            eaten_cards[max_index+1].append(p)
            max_index += 1
            index = max_index
        else:
            sg.update(p, (p, index))
            sg.update(min_x, (ide_ele, index))
            eaten_cards[index].append(p)
        if len(eaten_cards[index]) == K:
            sg.update(p, (ide_ele, index))
            for card in eaten_cards[index]:
                eaten_turns[card] = i+1
    for i in range(N):
        print(eaten_turns[i])
    
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