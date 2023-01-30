### Python code
# Description

This Question is transversal question in which we choose all the borders and apply DFS or BFS

## My approach

My approach was to apply DFS from the borders and keep a visited array so that the regions we visited from corner should not be conquered and converted to 'X'
In the improvement we removed the visited array and replaced by '-' so that we dont need a visited array and improved the space complexity

```
DFS Function consist of ways 
Marking it as visited
steps = [[-1,0],[1,0],[0,1],[0,-1]]
This represents up , down , right ,left direction 
We check if the steps + current cell is only in the 
right way and not in illegal cell
The space and time complexity of the approach is as follows
O(MXN) with the extra visited array of same complexity and Time complexity as O(MN)
The improvement in space and time complexity are as follows
O(MXN) without the extra visited array and TC as O(MN)
```


## Contribution
Peer review


