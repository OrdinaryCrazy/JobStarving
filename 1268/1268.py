import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#-------------------------------------------------------------------
        echos = []
        products.sort()
        prefix = ""
        for c in searchWord:
            prefix += c
            idx = bisect.bisect_left(products, prefix)
            echo = []
            for i in range(idx, min(idx + 3, len(products))):
                if products[i][:len(prefix)] == prefix:
                    echo.append(products[i])
            echos.append(echo)
        return echos
#-------------------------------------------------------------------     
#         root = {}
#         products.sort()
        
#         for product in products:
#             pointer = root
#             for c in product[:-1]:
#                 if c not in pointer:
#                     pointer[c] = ({}, None)
#                 pointer, word = pointer[c]
                    
#             if product[-1] in pointer:
#                 p, w = pointer[product[-1]]
#                 pointer[product[-1]] = (p, product)
#             else:
#                 pointer[product[-1]] = ({}, product)
        
#         def traverse(root):
#             firstThree = []
#             stack = [root]
            
#             while len(firstThree) < 3 and stack:
#                 childrens, word = stack.pop()
#                 if word:
#                     firstThree.append(word)
#                 childrens_keys = list(childrens.keys())
#                 childrens_keys.sort(reverse=True)
#                 for child in childrens_keys:
#                     stack.append(childrens[child])
                    
#             return firstThree
                    
#         pointer = root
#         echos = []
#         for c in searchWord:
#             if c in pointer:
#                 echos.append(traverse(pointer[c]))
#                 pointer, _ = pointer[c]
#             else:
#                 echos.append([])
#                 pointer = {}
        
#         return echos