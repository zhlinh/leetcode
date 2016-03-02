第一版的思路是先将nums1往后移动n位。

只要把nums2全部装进nums1后，剩下的就是排好序的了。

submit的结果为:
```
59 / 59 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第二版的思路是从后面一个开始添加，这样就不用初始化地移动了。

submit的结果为:
```
59 / 59 test cases passed.
Status: Accepted
Runtime: 52 ms
```
