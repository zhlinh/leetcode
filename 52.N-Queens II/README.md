第一版用的是DFS。需要考虑的是45度斜线和135度斜线的唯一表示。

45度的表示为row + col， 135度的表示为 n - 1 + row - col(n为矩阵的维数)。

还有个比较麻烦的是results添加时需要添加一个新复制的值，而不能是指针。

因为如果是指针，则后面会改变results的值。

不能简单地用result[:]，因为result的元素不是简单值而是List，复制的还是其指针。

所以就只好每次生成新的result，然后传递进下一层递归函数。

跟上一题(51.N-Queens)一样的解法，只是返回值是解法的数量。

submit的结果为:
```
9 / 9 test cases passed.
Status: Accepted
Runtime: 64 ms
```
