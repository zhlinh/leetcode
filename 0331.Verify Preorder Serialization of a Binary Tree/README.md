用了stack，这也是比较容易想到的。

很明显地观察到如果子节点出现连续两个#则可以pop掉当前的节点。

但子节点只有一个或没有#的该如何处理呢？这个是问题的关键。

可以想到子节点出现两个#的时候不是pop掉当前节点，而是要将当前节点替换成#。

相当于该节点目前就pop掉为空了，以方便另一个子树也是#或者变为#的时候再进行下一步。

如果父节点为#则直接返回False，因为空节点无法承载子树。
父节点为非#时将父节点替换成#，再往下遍历。

即连续出现三次'#'则返回False。

最终如果只剩一个#时则返回True，否则返回False。

注意输入为“#,#”的处理，即进入pop循环时的stack长度必须大于等于3。

sumbmit的结果为:
```
149 / 149 test cases passed.
Status: Accepted
Runtime: 64 ms
```

第二版就是另外一种视角了。应用到了图论。相当赞的思路。

相当于每个节点都有入度和出度，除根节点没有入度外。

非空节点的入度为1，出度为2。

空节点的入度为1，出度为0。

这样每次遇到一个节点都加上其入度，然后减去其出度，其值都小于等于0的。

相当于每遇到一个非空节点都会出现两个出度，这时候-2。空节点则到此为止。

然后遇到下一个节点时再补上1个，此时+1。这过程中都是小于等于0的。

初始值应设为-1，为了让root节点也能放到循环中入度+1。

最终如果全程没出现大于0的情况，则返回最后的统计结果是否等于0。

sumbmit的结果为:
```
149 / 149 test cases passed.
Status: Accepted
Runtime: 48 ms
```
