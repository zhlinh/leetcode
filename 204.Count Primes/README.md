看了别人的答案才知道的，还是easy题，囧。。。

自己用O(n^2)的方法明显LTE了。

这方法简直太聪明了，O(n)的时间复杂度。

先定义一个长度为n的数组primes，初始化True。

先定义res为1，然后以i=3为第一个查找元素，从i*i开始i的倍数的下标的primes赋值为False。

每找到一个primes[i]为True的，res+=1。

还有一点就是如果i > math.sqrt(n)，则不再作primes赋值的工作。

当然去掉这个判断也是可以的，因为那时候i*i肯定大于n了。

但这样也可以避免以后多次计算i*i。

submit的结果为:
```
20 / 20 test cases passed.
Status: Accepted
Runtime: 672 ms
```
