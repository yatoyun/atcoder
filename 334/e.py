from atcoder.modint import Modint, ModContext

from collections import defaultdict

class UnionFind():
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

def main():
    H, W = mapint()
    grid = [lstr() for _ in range(H)]
    
    uf = UnionFind(H*W-1)
    
    ignore_sum = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j]==".":
                ignore_sum += 1
                continue
            errprint(i, j)
            if i+1<H and grid[i+1][j]=="#":
                uf.unite(i*W+j, (i+1)*W+j)
            if j+1<W and grid[i][j+1]=="#":
                uf.unite(i*W+j, i*W+j+1)
    sum_nums = 0
    len_nums = 0
    curr_num_root = uf.group_size() - ignore_sum
    errprint(uf.roots())
    errprint(curr_num_root, uf.group_size(), ignore_sum)
    for i in range(H):
        for j in range(W):
            if grid[i][j]=="#":
                continue
            connect_set = set()
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = i+dx, j+dy
                if not(0<=nx<H and 0<=ny<W) or grid[nx][ny]==".":
                    continue
                root = uf.find(nx*W+ny)
                connect_set.add(root)
            sum_nums += curr_num_root - len(connect_set) + 1
            len_nums += 1
            errprint(sum_nums, len_nums)
    mod = 998244353
    errprint(sum_nums, len_nums)
    with ModContext(mod):
        ans = Modint(sum_nums)
        ans *= Modint(len_nums).inv()
        print(ans.val())
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
