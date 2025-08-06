from typing import List
import bisect

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return min(self.query(2 * node + 1, start, mid, l, r),
                   self.query(2 * node + 2, mid + 1, end, l, r))
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node + 1, start, mid, idx, val)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, val)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        
        # Create sorted baskets with original indices
        sorted_baskets = sorted((baskets[i], i) for i in range(n))
        capacities = [cap for cap, _ in sorted_baskets]
        original_indices = [idx for _, idx in sorted_baskets]
        
        # Create reverse mapping: original_index -> position in sorted array
        idx_to_pos = {original_indices[i]: i for i in range(n)}
        
        # Initialize segment tree with original indices
        seg_tree = SegmentTree(original_indices)
        
        unplaced = 0
        
        for fruit in fruits:
            # Binary search for first basket with enough capacity
            pos = bisect.bisect_left(capacities, fruit)
            
            if pos == n:
                # No basket can hold this fruit
                unplaced += 1
                continue
            
            # Query segment tree for minimum original index from pos to n-1
            min_idx = seg_tree.query(0, 0, n - 1, pos, n - 1)
            
            if min_idx == float('inf'):
                # No available basket found
                unplaced += 1
            else:
                # Use reverse mapping to find position instantly
                sorted_pos = idx_to_pos[min_idx]
                seg_tree.update(0, 0, n - 1, sorted_pos, float('inf'))
        
        return unplaced