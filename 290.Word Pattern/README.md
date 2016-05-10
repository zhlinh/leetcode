因为是双向映射，所以需要比较键和值映射的唯一性。

一开始用dic保存键值对patter->str和值键str->pattern对，然后就可以比较。

后来发现值str有可能等于键pattern，这样就会出问题。

然后想到把值str的最后加上“#”，这样就保证了不与键pattern相等。

最后还是用了两个dic，就不用再加”#“了，觉得可能每次要产生一个新的str会比较慢。

但试了下，时间都差不多，都挺慢的。

submit的结果为:
```
29 / 29 test cases passed.
Status: Accepted
Runtime: 48 ms
```
