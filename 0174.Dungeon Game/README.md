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

第二版的思路和第一版一样的，只是把二维的DP改成了一维的。

只要把握好哪个是二维空间里的下面一个元素和右边一个元素就好了。

另外需要注意起点的初始化问题就好。

submit的结果为:
```
44 / 44 test cases passed.
Status: Accepted
Runtime: 60 ms
```
