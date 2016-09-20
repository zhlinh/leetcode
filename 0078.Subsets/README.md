第一版用了DFS。

submit的结果为:
```
26 / 26 test cases passed.
Status: Accepted
Runtime: 52 ms
```

第二版只用了循环。

例如nums=[1, 2, 3]。思路是这样的:

init: [[]]
add 1: [[], [1]];
add 2: [[], [1], [2], [1, 2]];
add 3: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

submit的结果为:
```
26 / 26 test cases passed.
Status: Accepted
Runtime: 60 ms
```

第三版用了bit Manipulation。其实是和第二版的思路相似的。

只是会一开始就生成2^n个空list，然后再根据各元素应出现的位置对号入座。

例如nums=[1, 2, 3]:

[], [], [], [], [], [], [], []

[], [1], [], [1], [], [1], [], [1]

[], [1], [2], [1, 2], [], [1], [2], [1, 2]

[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]

submit的结果为:
```
26 / 26 test cases passed.
Status: Accepted
Runtime: 52 ms
```
