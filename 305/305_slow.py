class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        out = []
        root = [-1] * (m * n)
        cur_num_land = 0
        
        def find(root:List[int], root_id) -> int:
            if root_id == root[root_id]:
                return root_id
            else:
                return find(root, root[root_id])
        
        for r, c in positions:
            idx = r * n + c
            if root[idx] != -1:
                out.append(cur_num_land)
                continue
            
            cur_num_land += 1
            root[idx] = idx
            
            if r - 1 >= 0: 
                sur_idx = (r - 1) * n + c
                if root[sur_idx] != -1:
                    p = find(root, sur_idx); q = find(root, idx)
                    if p != q:
                        root[p] = q; cur_num_land -= 1
            if r + 1 < m: 
                sur_idx = (r + 1) * n + c
                if root[sur_idx] != -1:
                    p = find(root, sur_idx); q = find(root, idx)
                    if p != q:
                        root[p] = q; cur_num_land -= 1
            if c - 1 >= 0: 
                sur_idx = r * n + c - 1
                if root[sur_idx] != -1:
                    p = find(root, sur_idx); q = find(root, idx)
                    if p != q:
                        root[p] = q; cur_num_land -= 1
            if c + 1 < n: 
                sur_idx = r * n + c + 1
                if root[sur_idx] != -1:
                    p = find(root, sur_idx); q = find(root, idx)
                    if p != q:
                        root[p] = q; cur_num_land -= 1
            
            out.append(cur_num_land)
        
        return out
                
        
        
        
        
            
        