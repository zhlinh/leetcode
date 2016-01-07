看到已排序的list就想到了分治法里的Merge，然后时间复杂度为O(m+n)。

题目的要求为O(log(m+n))，可能就因为这个原因，该题的难度为hard。

决定先提交用Merge解法的版本。

发现在防止list越界上花了不少功夫，囧。

submit的结果为:
```
2079 / 2079 test cases passed.
Status: Accepted
Runtime: 124 ms
```

然后看了别人的答案，发现了用尾部递归的方法，可以达到O(log(min(m,n)))。

submit的结果为:
```
2079 / 2079 test cases passed.
Status: Accepted
Runtime: 118 ms
```

最后采用了一种不用递归的方法，时间复杂度为O(log(min(m,n)))。

思路如下，先观察一个图。

```
           LeftPart            |            RightPart
{ A[0], A[1], ... , A[i - 1] } | { A[i], A[i + 1], ... , A[m - 1] }
{ B[0], B[1], ... , B[j - 1] } | { B[j], B[j + 1], ... , B[n - 1] }
```

需要保证左右两边的元素个数相等，且右边的元素值比左边的都大。

即：

1. i+j = m-i+n-j,或者i+j = m-i+n-j+1（保证当为奇数时左边的比右边的多一个）

   且i = 0~m，之后可以定位i = imin~imax 所以j = (m+n+1)/2-i = half_len-i

2. A[i] > B[j-1] 且 B[j] > A[i-1]

通过二分法令i=(imin+imax)/2

再一个需要注意的就是当不满足条件时，imin和imax的左右移动

满足上述两条件时，分情况讨论总长为奇偶时的返回值

submit的结果为:
```
2079 / 2079 test cases passed.
Status: Accepted
Runtime: 100 ms
```

