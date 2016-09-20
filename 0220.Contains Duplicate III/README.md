使用了buckets，这样如果落于同一个buckets或者相邻的buckets且差距小于t则返回True。

buckets的范围为t+1，如t=3，则数值为0,1,2,3的都归到下标为0的bucket中。

dic[nums[i]//(t+1)] = nums[i]。

用dic作为buckets，而且需要及时删除不在滑动窗口内的元素。

如果dic的插入操作为log(n)，则

时间复杂度为O(nlog(n))。

submit的结果为:
```
30 / 30 test cases passed.
Status: Accepted
Runtime: 56 ms
```
