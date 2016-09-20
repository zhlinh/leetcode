字典树/前缀树中不是每个节点都代表word。

故需要用一个isWord，只有插入的word的最后一个字母才将其赋为True。

另外每一个节点都有一个长度为26的children数组，代表下一层节点。

然后还定义了一个val，当然不用这个也是可以的。此题中用key就可以表示val。

后来把数组改为dic，发现用时差不多。

submit的结果为:
```
14 / 14 test cases passed.
Status: Accepted
Runtime: 396 ms
```

第二版去掉了val，把数组换成了dic，这样可以节约空间。

submit的结果为:
```
14 / 14 test cases passed.
Status: Accepted
Runtime: 327 ms
```
