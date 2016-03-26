第一版用了Trie前缀树加DFS。

DFS的时候传进去的参数除了result[路径], results[最终结果集]，还有一个TrieNode。

这样就不用每次都serach或者startsWith来判断result了。

所以一开始初始化完Trie后，取得其trie.root作为node传进去。

避免添加重复项的方法可以将results设为set，就可以避免重复。

此处用的是添加result后，将result的当前node的isWord设置为False。

这样就有效地避免了重复添加。

submit的结果为:
```
37 / 37 test cases passed.
Status: Accepted
Runtime: 688 ms
```

第二版将Trie的search和startsWith去掉了。

然后将Trie的isWord改为了word。

然后在insert的最后将所添加的word赋给本节点的word。

这样就可以不用向DFS传递res路径了，只要某个节点的word存在则添加到results中。

然后将此节点的word设为None，以避免重复添加。
submit的结果为:
```
37 / 37 test cases passed.
Status: Accepted
Runtime: 642 ms
```
