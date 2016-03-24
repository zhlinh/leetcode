用了一个dic，需要注意的是一个值不能被map到不同的可以中。

即s=”ab”, t=”aa”应该要返回False。

所以当key不存在时，还应检查t[i]是否在dic的values()中。

submit的结果为:
```
30 / 30 test cases passed.
Status: Accepted
Runtime: 60 ms
```
