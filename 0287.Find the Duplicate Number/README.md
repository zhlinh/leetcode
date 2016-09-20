不得不说这真的是神一般的思路。

这个是用bit运算解不了的。因为重复的个数不定。

然后用的是类似找出142.Linked List Cycle II的循环开始点的思路。

真的是太赞了。

fast = nums[nums[fast]]，相当于fast = fast.next.next
slow = nums[slow]，相当于slow = slow.next。

因为nums[i]的值都可以作为下标，这样就形成了一个循环列表，当nums[i]有重复时。

因为nums[i]大于等于1，所以不用考虑会在i = 0时重复，故可以用nums[0]的下标作为起点。

如[1, 2, 3, 4, 2, 5]可以看成:

    1 -> 2 -> 3 -> 4
         |         |
           <- -- --

submit的结果为:
```
53 / 53 test cases passed.
Status: Accepted
Runtime: 56 ms
```
