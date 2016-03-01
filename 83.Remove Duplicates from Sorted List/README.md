第一版只用了两个index。

让p跑到与前面一个元素不相同的元素下，然后判断l.next是否等于p。

若相等，l = l.next。若不等，l.next = p, l = l.next。

l.next = p表示跳过删去的那些元素，l = l.next表示接受了当前的p。

submit的结果为:
```
166 / 166 test cases passed.
Status: Accepted
Runtime: 60 ms
```
