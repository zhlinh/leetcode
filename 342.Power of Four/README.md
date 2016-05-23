是4的pow必然是2的pow，即num>0且bit位只有一个1(num&(num-1)==0)。

另外bit位的1只出现在奇数位置，
所以可以用num & 0x55555555 != 0来排除仅是2的pow而不是4的pow。

当然最后一个排除仅是2的pow的方法还可以是(num-1) % 3 == 0。

sumbmit的结果为:
```
1060 / 1060 test cases passed.
Status: Accepted
Runtime: 72 ms
```
