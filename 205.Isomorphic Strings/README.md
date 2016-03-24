用了一个dic，需要注意的是一个值不能被map到不同的可以中。

即s=”ab”, t=”aa”应该要返回False。

所以当key不存在时，还应检查t[i]是否在dic的values()中。

submit的结果为:
```
30 / 30 test cases passed.
Status: Accepted
Runtime: 60 ms
```

第二版用了两个长度为256的数组m1，m2，char的常用解法，取其ascii码。

然后分别赋值为当前index+1，如果m1[s[i]] != m2[t[i]]时返回False。

这样用两个数组就很好地保证一一对应的关系。

因为无论是s[i]还是t[i]曾经出现过，再出现的时候如果不对应则他们的值肯定不相等。

这样就没有了一个值绑定两个值的情况。

submit的结果为:
```
30 / 30 test cases passed.
Status: Accepted
Runtime: 75 ms
```
