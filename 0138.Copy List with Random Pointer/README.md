用了DFS的方法。

需要用一个dic记录已生成过的节点。

木有写测试。

请到LeetCode页面进行测试:

[LeetCode-138.Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer)

时间复杂度为O(n)。

sumbmit的结果为:
```
11 / 11 test cases passed.
Status: Accepted
Runtime: 136 ms
```

第二版用了一个空间为O(1)的，即不用dic。

思路分为3步：

1. 将A->B->C 变为 A->A'->B->B'->C->C'
2. 令n'.random = n.random.next
3. 将复制序列抽取出来，n.next = n.next.next; n'.next = n'.next.next

每一步都需要将序列遍历一次。

时间复杂度为O(n)。

sumbmit的结果为:
```
11 / 11 test cases passed.
Status: Accepted
Runtime: 128 ms
```
