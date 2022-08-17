class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Tire
        root = [{}, None]
        for word in words:
            cur = root[0]
            for char in word[:-1]:
                if char not in cur:
                    cur[char] = [{}, None]
                cur = cur[char][0]
            if word[-1] not in cur:
                cur[word[-1]] = [{}, word]
            else:
                cur[word[-1]][1] = word
        
        # print(root)
        
        n = len(board)
        m = len(board[0])
        out = []
        
        def walk(sx, sy, node):
            if (sx < 0 or sx >= n or sy < 0 or sy >= m or board[sx][sy] == "#"):
                return
            if board[sx][sy] not in node[0]:
                return 
            
            next_node = node[0][board[sx][sy]]
            
            if next_node[1] is not None:
                out.append(next_node[1])
                next_node[1] = None
                
            if len(next_node[0]) == 0:
                return
            
            temp = board[sx][sy]
            board[sx][sy] = "#"
            walk(sx - 1, sy, next_node)
            walk(sx + 1, sy, next_node)
            walk(sx, sy - 1, next_node)
            walk(sx, sy + 1, next_node)
            board[sx][sy] = temp
        
        for i in range(n):
            for j in range(m):
                walk(i, j, root)
        
        return out
                    
        
#         # def find(board, word, source_i, source_j, k):
        
#         char_position_dict = {}
        
#         for i, row in enumerate(board):
#             for j, char in enumerate(row):
#                 if char not in char_position_dict:
#                     char_position_dict[char] = [(i, j)]
#                 else:
#                     char_position_dict[char].append((i, j))
        
#         matched_words = []
#         # print(char_position_dict)
        
#         for word in words:
#             valid = True
#             # for i in range(len(word)):
#             for char in set(word):
#                 # if word[i] not in char_position_dict:
#                 if char not in char_position_dict:
#                     valid = False
#             if not valid:
#                 continue
#             char_position_list_stack = []
#             for position in char_position_dict[word[0]]:
#                 char_position_list_stack.append([position])
                
#             while char_position_list_stack:
#                 last_position_list = char_position_list_stack.pop()
#                 if len(last_position_list) == len(word):
#                     matched_words.append(word)
#                     break
#                 k = len(last_position_list)
#                 # if word[k] not in char_position_dict:
#                 #     break
#                 for position in char_position_dict[word[k]]:
#                     if position in last_position_list:
#                         continue
#                     if position[0] - 1 == last_position_list[-1][0] and position[1] == last_position_list[-1][1]:
#                         char_position_list_stack.append(last_position_list + [position])
#                     if position[0] + 1 == last_position_list[-1][0] and position[1] == last_position_list[-1][1]:
#                         char_position_list_stack.append(last_position_list + [position])
#                     if position[1] - 1 == last_position_list[-1][1] and position[0] == last_position_list[-1][0]:
#                         char_position_list_stack.append(last_position_list + [position])
#                     if position[1] + 1 == last_position_list[-1][1] and position[0] == last_position_list[-1][0]:
#                         char_position_list_stack.append(last_position_list + [position])
        
#         return matched_words
            
                