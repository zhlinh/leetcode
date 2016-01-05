最容易想到的还是时间复杂度为O(n^2)的解法，相当于一个index从第一个开始，

另一个index从第一个index处开始，然后就被狠狠的虐了。

Submission Result: Time Limit Exceeded

Last executed input:

```
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./
:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567
89!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwx
yzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdef
ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@
[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$
...省略300多行(无换行符)，31655个字符...”
```

后来提交了一版，也是O(n^2)，但这次的第二个循环只用来更新dict。

通过了，但效率还是太低。

submit的结果为:
```
981 / 981 test cases passed.
Status: Accepted
Runtime: 432 ms
```