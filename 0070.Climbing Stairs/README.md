用的排列组合的数学方法解的，看到只问个数，就想到数学方法了。

时间复杂度为O(n^2)。

submit的结果为:
```
45 / 45 test cases passed.
Status: Accepted
Runtime: 40 ms
```

第二版用的fibonacci(斐波那契数列)来解的。

即可以想到res(n) = res(n-1) + res(n-2)。

即分为前进一步或前进两步两种。

当然这也是DP的思想，不过不需要维护一个数组，只需维护3个变量即可。

时间复杂度为O(n)。

submit的结果为:
```
45 / 45 test cases passed.
Status: Accepted
Runtime: 44 ms
```
