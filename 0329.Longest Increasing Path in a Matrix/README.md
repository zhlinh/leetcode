很容易想到DFS。

但开始就纯粹的用不同的起点开始dfs，然后就超时了。

想用cache，然后还一个劲地在想重复问题。

后来发现这个不可能会重复，后面的点不会再往前面的点走，因为只会往更大的方向走。

之前还将当前点变为其他值以防重复，真的是想多了。。。

无重复这就可以很容易用一个二维的cache了，记录当前点出发的最大length值。

这样就解决了超时问题。

sumbmit的结果为:
```
137 / 137 test cases passed.
Status: Accepted
Runtime: 392 ms
```