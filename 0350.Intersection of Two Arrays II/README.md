求两个数组的公共元素，包含重复元素。

此时就不能使用set了，否则不能体现某个数组的重复元素数量，
所以可以是用dic来解决这一问题。

初始化dic，然后只有找到dic[num]大于0才算有公共元素。

另一种方法是先将两个数组排序，然后用两个index，相同的话就加入。

sumbmit的结果为:
```
60 / 60 test cases passed.
Status: Accepted
Runtime: 52 ms
```
