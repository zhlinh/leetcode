第一版用了BIT(Bynary Indexed Trees)。

相当于用一个数组A[i]用来存储i的个数。B[i]则是BIT，用来计算A[0]到A[i]的和。
这样就可以计算出小于i的值。

所以数组B的大小要等于max(i)+1。

这样就可以从右往左遍历nums[j] = i，然后更新A[i]的值，将其加1。
然后更新含有A[i]值的B[i]。

实际上并不需要维护A[i]，只需每次都以nums[j]来更新相应的B[i]即可，使其加1即可。

即：
```
B[1] = A[1]
B[2] = A[1] + A[2]
B[3] = A[3]
B[4] = A[1] + A[2] + A[3] + A[4]
B[5] = A[5]
B[6] = A[5] + A[6]
B[7] = A[7]
B[8] = A[1] + A[2] + A[3] + A[4] + A[5] + A[6] + A[7] + A[8]
...
```

即A[0]和B[0]始终为0，用来辅助计算小于最小值1的个数和。

这样数组B实际从1开始，BIT的本质是下标必须含有1，否则无法加上lowbit进入别的下标。

所以B[1] = A[1]。但有些情况组织成B[1] = A[0]，与其说令k = i + 1，
不如将A的下标加上1，使B的下标从1开始，即都可以统一成B[i] = A[i]。
只需抓住B[i]从i = 1开始的实质，便比较好理解了。

需要注意的是需要避免i有负数，所以将以最小值为基准1，然后其他数相应增加。

这样既保持原有的顺序，又保证每一个数为非负数。

这样每次用update来更新现在各个数出现的次数，再用getSum来得到小于当前数的个数和。

这便是题目所求。

时间复杂度为O(nlog(maxNum))。

当maxNum很大时会耗费比较多的时间，且负数很大时，可能会越界。
所以数组B的长度有最好用长整形long。

```
当然可以优化，先排序，然后将其大小和下标建立一个map。
然后就可以从右往左逐一把map[nums[i]]更新到B中，然后在sumRange了。
这样就可以使时间复杂度变为O(nlog(n))。
```

submit的结果为:
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 192 ms
```

第二版用了合并排序mergeSort的方法。另外还可以使用BST(Binary Search Trees)。

思路是用mergeSort的方法排序一遍原nums。

仅需要在排序的过程中判断当左侧数的小于等于右侧的数时，
需要记录下此次merge中已经merge进新序列的右侧的数的个数，
这些处于当前左侧数的右侧且小于等于当前左侧数，即题目所求。

所以另外需要记录下原nums的数和下标的对应关系，
可以用一个二维数组numsWithIndex[n][2]表示，[i][0]存储位置，[i][1]存储数值。
这样就可以在排序numsWithIndex的过程中直接把符合题目所求的个数累加到相应的res位置中。

可以从最初往下递归到最后排序2个数来考虑，如果逆序则加1，
然后排序后的序列会作为左侧left序列。

然后不断地往上return到排序左右各一半的序列，即逐渐把逆序的个数累加的过程。

时间复杂度为O(nlog(n))。

submit的结果为:
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 288 ms
```
