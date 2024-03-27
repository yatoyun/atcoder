import sys
from collections import defaultdict
input = sys.stdin.readline

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
        return [i for i, x in enumerate(self.root) if x < -1]

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


def calc_index(x,y,W):
    return x + y*W
def unite(x,y,W,uf,sensors_set,node):
    next_node = calc_index(x,y,W)
    uf.unite(node, next_node)
    if node in sensors_set:
        sensors_set.remove(node)
    if next_node in sensors_set:
        sensors_set.remove(next_node)

def main():
    H, W = map(int, input().split())
    graph = [list(input().strip()) for _ in range(H)]
    
    uf = UnionFind(H*W)
    sensors_set = set()
    for i in range(H):
        for j in range(W):
            if graph[i][j] != "#":
                continue
            node = calc_index(j,i,W)
            sensors_set.add(node)
            if i > 0 and graph[i][j] == graph[i-1][j]:
                unite(j,i-1,W,uf,sensors_set,node)
            if i > 0 and j > 0 and graph[i][j] == graph[i-1][j-1]:
                unite(j-1,i-1,W,uf,sensors_set,node)
            if i > 0 and j < W-1 and graph[i][j] == graph[i-1][j+1]:
                unite(j+1,i-1,W,uf,sensors_set,node)
            if j > 0 and graph[i][j] == graph[i][j-1]:
                unite(j-1,i,W,uf,sensors_set,node)
    print(uf.group_size()+len(sensors_set))


if __name__ == "__main__":      
    main()
