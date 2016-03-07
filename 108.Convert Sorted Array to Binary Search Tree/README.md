第一版用了递归的方法。

又因为是排好序的，所以很容易想到二分法。

subimt的结果为:
```
32 / 32 test cases passed.
Status: Accepted
Runtime: 96 ms
```

第二版用了循环的方法。只是为了实现一下递归。

用了3个stack，一个存放TreeNode，另两个分别为start和end。

值得注意的是当l <= mid - 1或r >= mid + 1时才进行下一步相应的划分。

subimt的结果为:
```
32 / 32 test cases passed.
Status: Accepted
Runtime: 104 ms
```
