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
