第一版用了递归，因为中序遍历的直观定义就是用递归来表示的。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 52 ms
```

第二版用的是循环，相当赞的思路，用了一个stack。

会一路左子树入stack，然后pop，然后加入res，然后右子树入stack，然后再循环。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 36 ms
```
