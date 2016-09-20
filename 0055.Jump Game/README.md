第一版还是利用curMax和nextMax的思路来划分level。

时间复杂度为O(n)。

submit的结果为:
```
72 / 72 test cases passed.
Status: Accepted
Runtime: 72 ms
```

第二版只用了一个reach来保存最大能到达的下标，然后i <= reach即为可到达。

时间复杂度为O(n)。

submit的结果为:
```
72 / 72 test cases passed.
Status: Accepted
Runtime: 60 ms
```
