已经想到用stack。但还是有两处问题。

1. 自己想的是用stack存list，而最好应该逆序逐个存list中的NestedInteger。

2. 自己想的在next()将int放到最前然后才可以返回，但最好是在hasNext()中完成
在将int型的NestedInteger放到最前，然后在next()中pop再返回即可。
如果stack为空则返回False，找到int型的NestedInteger则返回True。

因为需要实现NestedInteger，所以这次就没写test.py文件，
可以直接去[Leetcode官网](https://leetcode.com/problems/flatten-nested-list-iterator/)测试。

sumbmit的结果为:
```
44 / 44 test cases passed.
Status: Accepted
Runtime: 138 ms
```
