class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        stack = [(sx, sy)]
        while stack:
            x, y = stack.pop()
            if x == tx and y == ty:
                return True
            if x + y <= tx:
                stack.append((x + y, y))
            if x + y <= ty:
                stack.append((x, x + y))
        return False