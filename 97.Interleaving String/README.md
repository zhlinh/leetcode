第一版用了递归的方法。DFS。还得要避免TLE。

用了一个dic来记录当前访问的位置p1 * len(s3) + p2，即一个独一为二的的值。

这样就可以避免很多的重复访问，因为回溯的时候还可能再重复该点。

另外用的是判断s1或s2结束时，s2或s1的剩余字符串是否与s3的剩余字符串相等。

这样可以更快一些，而不是等到s3结束时再判断。

时间复杂度为O(mn)

submit的结果为:
```
101 / 101 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第二版用了DP，居然一开始没有想到用这个。

需要注意的是一开始要判断s3的长度是否等于s1和s2的长度之和。

很容易理解，不过速度比第一版慢多了。

时间复杂度为O(mn)

submit的结果为:
```
101 / 101 test cases passed.
Status: Accepted
Runtime: 88 ms
```

第三版用了BFS，当然可以很容易变为DFS，将BFS的pop(0)改为pop()就是DFS了。

就是Queue变为Stack。

也是要避免重复用了一个dic记录当前访问位置。

时间复杂度为O(mn)。

但总的来说并不需要每次都是mn，所以会比DP快。

submit的结果为:
```
101 / 101 test cases passed.
Status: Accepted
Runtime: 56 ms
```
