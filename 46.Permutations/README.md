第一版用了DFS，这也是最容易想到的方法。

submit的结果为:
```
25 / 25 test cases passed.
Status: Accepted
Runtime: 96 ms
```

第二版也是DFS，别问为什么。

但这次有所改变，通过调换nums元素的位置然后添加nums来达到排列的目的。

而不用判断元素是否重复添加。

传递了一个表示当前depth的参数。

submit的结果为:
```
25 / 25 test cases passed.
Status: Accepted
Runtime: 72 ms
```

第三版用了BFS，就是不断地通过调换别的元素到当前位置来扩充叶子节点的规模。

submit的结果为:
```
25 / 25 test cases passed.
Status: Accepted
Runtime: 80 ms
```
