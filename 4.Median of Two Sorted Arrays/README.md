看到已排序的list就想到了分治法里的Merge，然后时间复杂度为O(m+n)。

题目的要求为O(log(m+n))，可能就因为这个原因，该题的难度为hard。

决定先提交用Merge解法的版本。

发现在防止list越界上花了不少功夫，囧。

submit的结果为:
```
2079 / 2079 test cases passed.
Status: Accepted
Runtime: 124 ms
```
