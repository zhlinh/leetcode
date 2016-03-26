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
