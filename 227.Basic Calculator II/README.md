用了一个stack。

这次是只有加减乘除没有括号。

判断符号需要滞后，即记录的是前一个的符号，这样才能进行有乘除的运算。

初始化符号为‘+’，因为第一个数如果是正数则需要先入栈。

将减当做符号，则加减的数就直接放到stack里。

而乘除需要将stack.pop() *或/ num放到stack里。因为不存在2 * -2的形式。

而python需另外考虑除的时候被除数为负数时如何取整的问题。将其转为abs再最后取负值。

最后将stack里的所有数都加起来。

当然也可以用一个preVal和一个curVal，这样就可以不用stack了。

submit的结果为:
```
109 / 109 test cases passed.
Status: Accepted
Runtime: 260 ms
```
