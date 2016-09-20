第一版用的是循环n &= (n-1)，退出条件为n等于0。

循环的次数即为1出现的次数。

这个其实就是减法异或的意思，每次都清除最末尾的1。

很犀利的解法。当然也可以用逐一移位来解知道n等于0，但没这个快。

submit的结果为:
```
600 / 600 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第二版用的比特流，O(1) space。

就是把1的个数都累加起来，依次加到2bit里，装到4bit里...装到32比特里。

最后得到的即为1出现的次数。

submit的结果为:
```
600 / 600 test cases passed.
Status: Accepted
Runtime: 52 ms
```
