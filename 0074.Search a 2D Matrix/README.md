其实就是一个已排序的序列，先用二分法找出所在行，然后再用同样的方法找出所在列。

时间复杂度为O(log(m) + log(n))。

submit的结果为:
```
134 / 134 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第二版将矩阵当做序列来解，利用`A[x] = matrix[x//n][x%n]`来解。

然后就可以转换为传统的二分法(l, r均在序列内，故用l<=r判断, l, r分别有+1,-1)。

时间复杂度为O(log(m) + log(n))。

submit的结果为:
```
134 / 134 test cases passed.
Status: Accepted
Runtime: 52 ms
```
