# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'
        currentNode = 0
        queue = [root]
        outString = '['
        while currentNode < len(queue):
            if queue[currentNode] is not None:
                outString += str(queue[currentNode].val) + ','
                queue.append(queue[currentNode].left)
                queue.append(queue[currentNode].right)
            else:
                outString += 'null,'
            currentNode += 1
    
        # while outString[-5:] == 'null,':
        #     outString = outString[:-5]
        
        outString = outString[:-1] + ']'
        return outString

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodeList = []
        valueList = data[1:-1]
        if valueList:
            valueList = [v.strip() for v in valueList.split(',')]
        else:
            return None
        if len(valueList) > 0:
            nodeList.append(TreeNode(int(valueList[0])))
        else:
            return None
        currentNode = 0
        currentValue = 1
        while currentValue < len(valueList):
            node = nodeList[currentNode]
            currentNode += 1
            
            v = valueList[currentValue]
            if v != 'null':
                nodeList.append(TreeNode(int(v)))
                node.left = nodeList[-1]
            currentValue += 1
            
            if not currentValue < len(valueList):
                break
                
            v = valueList[currentValue]
            if v != 'null':
                nodeList.append(TreeNode(int(v)))
                node.right = nodeList[-1]
            currentValue += 1
            
        return nodeList[0]
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))