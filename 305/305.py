class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        def find(root:List[int], root_id) -> int:
            if root_id == root[root_id]:
                return root_id
            else:
                return find(root, root[root_id])
            
        def Union(root:List[int], rank:List[int], idx, sur_idx):
            p = find(root, idx)
            q = find(root, sur_idx)
            if p == q:
                return False
            if rank[p] > rank[q]:
                root[q] = p
            elif rank[p] < rank[q]:
                root[p] = q
            else:
                root[q] = p
                rank[p] += 1
                
            return True
            
            
        out = []
        root = [-1] * (m * n)
        rank = [-1] * (m * n)
        visited = [False] * (m * n)
        cur_num_land = 0
        
        for i in range(m):
            for j in range(n):
                root[i * n + j] = i * n + j
        
        for r, c in positions:
            idx = r * n + c
            
            if visited[idx]:
                out.append(cur_num_land)
                continue
                
            cur_num_land += 1
            visited[idx] = True
            
            if r - 1 >= 0 and visited[idx - n] and Union(root, rank, idx, idx - n): 
                cur_num_land -= 1
            if r + 1 < m  and visited[idx + n] and Union(root, rank, idx, idx + n): 
                cur_num_land -= 1
            if c - 1 >= 0 and visited[idx - 1] and Union(root, rank, idx, idx - 1): 
                cur_num_land -= 1
            if c + 1 < n  and visited[idx + 1] and Union(root, rank, idx, idx + 1): 
                cur_num_land -= 1
            
            out.append(cur_num_land)
        
        return out
                
        
        
        
        
            
        