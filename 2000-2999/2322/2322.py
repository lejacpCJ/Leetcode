from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]

        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Compute subtree XOR values, parent relationships, and timestamps
        subtree_xor = [0] * n
        parents = [-1] * n
        enter_time = [0] * n
        exit_time = [0] * n
        time = 0

        def dfs(node, parent):
            nonlocal time
            parents[node] = parent
            enter_time[node] = time
            time += 1

            subtree_xor[node] = nums[node]
            for neigh in graph[node]:
                if neigh != parent:
                    dfs(neigh, node)
                    subtree_xor[node] ^= subtree_xor[neigh]
            
            exit_time[node] = time
            time += 1
        
        dfs(0, -1)
        total_xor = subtree_xor[0]

        def is_ancestor(a, b):
            return enter_time[a] <= enter_time[b] and exit_time[b] <= exit_time[a]

        min_score = float('inf')

        # Try all pairs of edges
        for i in range(len(edges)):
            u1, v1 = edges[i]

            # Make sure v1 is child of u1
            if parents[u1] == v1:
                u1, v1 = v1, u1
            
            for j in range(i + 1, len(edges)):
                u2, v2 = edges[j]

                # Make sure v2 is child of u2
                if parents[u2] == v2:
                    u2, v2 = v2, u2
                
                # Calculate XOR values of three components
                if is_ancestor(v1, v2):
                    # v2 is in subtree of v1
                    xor1 = subtree_xor[v2]
                    xor2 = subtree_xor[v1] ^ subtree_xor[v2]
                    xor3 = total_xor ^ subtree_xor[v1]
                elif is_ancestor(v2, v1):
                    # v1 is in subtree of v2
                    xor1 = subtree_xor[v1]
                    xor2 = subtree_xor[v2] ^ subtree_xor[v1]
                    xor3 = total_xor ^ subtree_xor[v2]
                else:
                    # Disjoint subtree
                    xor1 = subtree_xor[v1]
                    xor2 = subtree_xor[v2]
                    xor3 = total_xor ^ subtree_xor[v1] ^ subtree_xor[v2]
                
                max_xor = max(xor1, xor2, xor3)
                min_xor = min(xor1, xor2, xor3)
                min_score = min(min_score, max_xor - min_xor)
            
        return min_score