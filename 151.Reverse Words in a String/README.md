这道题估计是出给C语言的，直接修改str然后O(1)空间。

否则O(n)空间的会比较简单，即便是java也是另外生成一个字符串。

说一下如果是C，然后O(1)空间的思路。

需要避免行首多个空格，行中多个空格的情况，所以会用i和j两个索引。

j是有效的长度，然后反转遇到的每个word，然后在出现首个word后再加上空格。

然后将s.resize(j)，或者添加\0结束符。

最后再将整个字符串反转即为所求。

submit的结果为:
```
22 / 22 test cases passed.
Status: Accepted
Runtime: 40 ms
```