
def maximumDepthOfTree(self,root):
    if root ==None: 
        return 0
    return 1 + self.maximumDepthOfTree(root.left) + self.maximumDepthOfTree(root.right)

