主要修改了push，而且还用了另外一个stack作为临时变量。

submit的结果为:
```
17 / 17 test cases passed.
Status: Accepted
Runtime: 52 ms
```

第二版用了两个stack，非常聪明的方法。思路是这样的。

```
     <- <- <- <--  in_stack
    |
    |
     -> -> -> -->  out_stack
```

push的时候直接push到in_stack中。

peek和pop的时候如果out_stack为空则将in_stack的全部延箭头方向转移到out_stack中，
然后直接使用out_stack的peek和pop就可以了。

判断empty要判断in_stack和out_stack都为空。

submit的结果为:
```
17 / 17 test cases passed.
Status: Accepted
Runtime: 40 ms
```
