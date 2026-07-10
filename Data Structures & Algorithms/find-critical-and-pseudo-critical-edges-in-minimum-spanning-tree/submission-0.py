class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        # Add index
        edges = [e + [i] for i, e in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        def kruskal(skip_edge=-1, force_edge=-1):
            parent = list(range(n))
            rank = [1] * n

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                rx, ry = find(x), find(y)
                if rx == ry:
                    return False
                if rank[rx] < rank[ry]:
                    rx, ry = ry, rx
                parent[ry] = rx
                rank[rx] += rank[ry]
                return True

            weight = 0

            # force include edge
            if force_edge != -1:
                u, v, w, _ = edges[force_edge]
                if union(u, v):
                    weight += w

            for i, (u, v, w, _) in enumerate(edges):
                if i == skip_edge:
                    continue
                if union(u, v):
                    weight += w

            # check if fully connected
            root = find(0)
            if all(find(i) == root for i in range(n)):
                return weight
            return float('inf')

        # Original MST weight
        mst_weight = kruskal()

        critical = []
        pseudo = []

        for i in range(len(edges)):
            # If removing edge increases MST → critical
            if kruskal(skip_edge=i) > mst_weight:
                critical.append(edges[i][3])
            # If forcing edge keeps MST same → pseudo-critical
            elif kruskal(force_edge=i) == mst_weight:
                pseudo.append(edges[i][3])

        return [critical, pseudo]
