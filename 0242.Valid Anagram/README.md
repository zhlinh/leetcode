很容易想到用dic来解。

需要注意的是要先判断如果两个字符串的长度不相等，则直接返回False。
否则根据dic判断也会出错。

时间复杂度为O(n)。

当然也可以用数组来代替dic，如果都是小写字母的话。

还有种解法是先排序，然后判断两个字符串是否相等，当然这估计会很慢。

submit的结果为:
```
34 / 34 test cases passed.
Status: Accepted
Runtime: 72 ms
```
