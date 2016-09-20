用fast，slow两个索引，如果有循环，这fast一定会追上slow一圈，他们一定会相遇。

因为fast每次会比slow快一步。

此外还需要找出循环开始的点，这就需要额外的数学思维了。

每次fast都比slow快一步，假设slow和fast在圈内的m点相遇。

那么slow再次走到循环开始点(或加上n圈)则恰好等于entry从一开始走到循环开始点。

即相当于slow把之前fast比它快的恰好补回来了。

有可能加上n圈是因为之前非循环段太长，然后fast也在圈内绕了n圈，这并不影响结果。

```
16 / 16 test cases passed.
Status: Accepted
Runtime: 81 ms
```
