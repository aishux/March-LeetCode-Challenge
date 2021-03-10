def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        current_level = [root]
        next_level = []
        count = 1
        if d == 1:
            x = TreeNode(val=v,left=root)
            return x
        while count != d:
            for i in current_level:
                if i.right:
                    next_level.append(i.right)
                if i.left:
                    next_level.append(i.left)
            count += 1
            
            if count != d:
                current_level = next_level
                next_level = []
            
        for i in current_level:
            temp1 = i.left
            temp2 = i.right
            i.left = TreeNode(val=v,left=temp1,right=None)
            i.right = TreeNode(val=v,left=None,right=temp2)
            
        
        return root
