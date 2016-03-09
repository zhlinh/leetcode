第一版用了BFS。

```
14 / 14 test cases passed.
Status: Accepted
Runtime: 102 ms
```

第二版用了两个指针，指向上一层的第一个元素和上一层的所有元素。

然后就是简单的拼接了。

值得注意的是这种解法只有在perfect tree下才可行。

当然了，题目中已经有说明输入的树就是这种情况。

```
14 / 14 test cases passed.
Status: Accepted
Runtime: 92 ms
```
