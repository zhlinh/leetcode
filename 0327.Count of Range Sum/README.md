唉，表示只想到O(n^2)的方法，就是先得到sums数组，记录0到i的和。

sums[i+1] = sums[i] + nums[i]。

这样就可以用sums[i+1]-sums[j]得到i到j的和，包含i, j。

用两重循环判断就可以得到题目所求。

另一种思路是用mergeSort，有点像`315.count smaller number after self`那题。

那题是mergeSort的过程中统计右侧比左侧小的数。

而这题可以在mergeSrot的过程中统计a <= sums[j] - sums[i] <= b with j > i。
其中j在右侧，i在左侧。

这样就可以得到题目所求，时间复杂度为O(nlog(n))。

比直接统计快的秘诀是利用左侧和右侧已排序，这样就可以快速统计个数。

```
while i < m:
    while b < n and right[b] - left[i] < lower:
        b += 1
    while e < n and right[e] - left[i] <= upper:
        e += 1
    res += (e - b)
    i += 1
```

b记录符合条件>=lower的开端，e记录刚好不符合<=upper的结尾，

这样就可以得到从左侧的i到右侧的和符合条件的个数，即(e - b)。

且当循环下一个左侧的i时，b，e不用重新恢复起点，因为其一定是符合两个循环条件的。

因为left[i+1] > left[i]所以right[b或e] - left[i+1]会更小。

这就是比直接逐一统计快的关键原因。

这也让我再一次见识到了mergeSort可以做的事，
就是可以处理统计i到j的和或j比i小之类问题，

是分治的思想，但又利用了排序的好处。

sumbmit的结果为:
```
61 / 61 test cases passed.
Status: Accepted
Runtime: 392 ms
```

第二版就将mergeSort改了一下，改为在原序列上更改，添加start和end两个参数。

另外返回的是res。

其实mergeSort的关键在于当只有一个元素的时候就返回。

然后在原序列上改可以逐一把右侧中比左侧小的放进mergeList中，然后最后放当前左侧的数。
接着循环下一个左侧的数。

最后把mergeList[:k]复制到sums[start:k]，k后面的是没做更改的右侧的数。

不过和第一版用的时间很接近，貌似没什么优化，但算是学习mergeSort的另一种实现吧。

sumbmit的结果为:
```
61 / 61 test cases passed.
Status: Accepted
Runtime: 404 ms
```
