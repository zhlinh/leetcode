第一版用了DFS。

值得注意的是判定是否符合时需要无叶子节点时再判定。

即root.left == None and root.right == None。

```
114 / 114 test cases passed.
Status: Accepted
Runtime: 64 ms
```

第二版用了PostOrder后序遍历。

练习一下，需要注意的是需要用pre来记录上一次访问的叶子节点(无左右子树)。

当为叶子节点时赋值cur = None。

然后当下一次root.right != pre时才可赋值root = root.right。

```
114 / 114 test cases passed.
Status: Accepted
Runtime: 76 ms
```
