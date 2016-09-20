已经想到了用DP来解。每一个节点分为include和exclude两种情况，然后保留着两个的最大值。

但问题是我想的是用BFS来至顶向下来求每一层的每个元素的两个dp值。

以此压到另一个queue中，与维护BFS的queue保持一致就好。

然后在最后没有子节点时将两个dp的max值加到res中，这样虽然也可行但还是不够优雅。

这种情况明显是要自底向上求dp值，然后在根节点处取包含和不包含当前节点的max。

还可以用DFS递归的方法，返回两个dp值，实现自底向上返回，这样就不用分散地求和。

无cache的纯粹DFS：
虽然会很慢，但在初始阶段很容易理解include和exclude的思路。
```
def rob(root):
    if not root:
        return 0
    return max(robInclude(root), robExclude(root))

def robInclude(node):
    if not node:
        return 0
    return robExclude(node.left) + robExclude(node.right) + node.val

def robExclude(node):
    if not node:
        return 0
    return rob(node.left) + rob(node.right)
```


sumbmit的结果为:
```
134 / 134 test cases passed.
Status: Accepted
Runtime: 1160 ms
```
