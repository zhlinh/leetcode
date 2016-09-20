理解了什么是逆波兰表示法Reverse Polish Notation之后，实现就很简单了。

用一个堆栈即可解决问题。

数字压入堆栈，运算符则从堆栈中取出数字计算后将结果压入堆栈。

最后返回堆栈中的最后一个数。

对于python，除法的时候需要注意还是得先化为float然后再转为int。

否则遇到负数时，会出现6/-132等于-1而不是0。

submit的结果为:
```
20 / 20 test cases passed.
Status: Accepted
Runtime: 72 ms
```
