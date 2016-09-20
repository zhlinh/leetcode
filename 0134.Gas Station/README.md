第一版用了两个索引。

一个是start从最后一个开始，另一个是end从第一个开始。

然后需要计算的是total，若total>=0则end+=1，否则start-=1。

注意计算total和end/start加减1的顺序。

start-=1是为了去加油的，所以先start-=1，再计算total。

sumbmit的结果为:
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 44 ms
```
