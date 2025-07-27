# Given two arrays, val[] and wt[], representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
# Return the maximum value as a double, rounded to 6 decimal places.

# Examples :

# Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
# Output: 240.000000
# Explanation: Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0 Thus, total maximum value of item we can have is 240.00 from the given capacity of sack. 
# Input: val[] = [60, 100], wt[] = [10, 20], capacity = 50
# Output: 160.000000
# Explanation: Take both the items completely, without breaking. Total maximum value of item we can have is 160.00 from the given capacity of sack.

class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        n=len(val)
        items=[[val[i],wt[i]] for i in range(n)]
        items.sort(key=lambda x:x[0]/x[1],reverse=True)
        res=0.0
        currentcapacity=capacity
        for i in range(n):
            if items[i][1]<=currentcapacity:
                res+=items[i][0]
                currentcapacity-=items[i][1]
            else:
                res+=(1.0*items[i][0]/items[i][1]*currentcapacity)
                break
        return res
       
# Time Complexity: O(n log n) – due to sorting
# Space Complexity: O(n) – for storing item list with
