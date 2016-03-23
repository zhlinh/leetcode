一开始想到的就是DP，然后发现无法存储每个路径的历史最小值。

然后就用DFS，很容易就LTE了。

后来看了别人的答案，发现可以从终点触发，然后DP存的是在当前点所需的最小HP。

从最后开始是因为最后点的所需最小HP是已知的，就是1或者更大。

submit的结果为:
```
44 / 44 test cases passed.
Status: Accepted
Runtime: 72 ms
```
