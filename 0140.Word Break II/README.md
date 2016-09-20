如果直接用DFS，无疑会LTE的，因为会有大boss：

```
'aaaaa...aaaab', ['a', 'aa', 'aaa', ... 'aaa...aa']
```

或者

```
'baaaaaaaa...aaaa', ['a', 'aa', 'aaa', ..., 'aaa...aa']
```

所以得用一种有cache的DFS，即记录底部分支的有效路径，达到避免重复计算的目的。

这样就要求每一层设置一个新的res，记录本层以下的路径。

将截取剩余的s为key，res为值，存入cache中，然后return res。

每次DFS时先查找是否在cache中，如果有，则直接return存在cache中的值。

```
37 / 37 test cases passed.
Status: Accepted
Runtime: 64 ms
```
