先构造Trie前缀树，然后难点在于search。因为加入了’.’。

一开始就想到DFS，但想尝试用循环来写，发现是很难的。

堆栈内出了node还得有一个表示对应层级的i。

后来就用了递归的方法。

submit的结果为:
```
13 / 13 test cases passed.
Status: Accepted
Runtime: 556 ms
```

第二版用的是BFS，就是把每一层的可能符合的字母都添加进queue，直到最后一层。

将然后将最后一层的所有节点遍历，检查是否有isWord。如果有则返回True。否则为false。

submit的结果为:
```
13 / 13 test cases passed.
Status: Accepted
Runtime: 556 ms
```
