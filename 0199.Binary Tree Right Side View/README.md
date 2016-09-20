很容易想到的就是BFS，然后将每层的最后一个节点的值放入res中。

submit的结果为:
```
210 / 210 test cases passed.
Status: Accepted
Runtime: 58 ms
```

第二版用了DFS，就是先访问右子树，再访问左子树，res在每一层只添加第一个访问的节点。

通过len(res) == depth来判断处于当前层且从未添加节点。

submit的结果为:
```
210 / 210 test cases passed.
Status: Accepted
Runtime: 48 ms
```
