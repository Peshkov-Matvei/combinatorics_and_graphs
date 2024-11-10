import unittest


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
        if len(mst) == n - 1:
            break
    return mst


class TestKruskal(unittest.TestCase):
    def test_small_graph(self):
        n = 4
        edges = [
            (0, 1, 1),
            (0, 2, 4),
            (1, 2, 2),
            (1, 3, 3),
            (2, 3, 5)
        ]
        mst = kruskal(n, edges)
        self.assertEqual(sum(weight for _, _, weight in mst), 6)
        self.assertEqual(len(mst), n - 1)

    def test_disconnected_graph(self):
        n = 3
        edges = [
            (0, 1, 1)
        ]
        mst = kruskal(n, edges)
        self.assertNotEqual(len(mst), n - 1)

    def test_single_edge(self):
        n = 2
        edges = [
            (0, 1, 7)
        ]
        mst = kruskal(n, edges)
        self.assertEqual(sum(weight for _, _, weight in mst), 7)
        self.assertEqual(len(mst), n - 1)

    def test_large_graph(self):
        n = 6
        edges = [
            (0, 1, 1),
            (0, 2, 3),
            (0, 3, 4),
            (1, 2, 2),
            (1, 4, 6),
            (2, 3, 5),
            (3, 4, 7),
            (4, 5, 8),
            (3, 5, 9)
        ]
        mst = kruskal(n, edges)
        # Исправлено ожидаемое значение на 21
        self.assertEqual(sum(weight for _, _, weight in mst), 21)
        self.assertEqual(len(mst), n - 1)

if __name__ == '__main__':
    unittest.main()
