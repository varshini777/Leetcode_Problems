# Job Sequencing Problem
# You are given two arrays: deadline[], and profit[], which represent a set of jobs, where each job is associated with a deadline, and a profit. Each job takes 1 unit of time to complete, and only one job can be scheduled at a time. You will earn the profit associated with a job only if it is completed by its deadline.
# Your task is to find:
# The maximum number of jobs that can be completed within their deadlines.
# The total maximum profit earned by completing those jobs.
# Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
# Output: [2, 60]
# Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).

class k:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit
class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        jobs = []
        for i in range(n):
            jobs.append(k(i+1, deadline[i], profit[i]))  
        jobs.sort(key=lambda x: x.profit, reverse=True)
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)
        l = [-1] * (maxi + 1)
        c = 0
        curr_profit = 0
        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if l[j] == -1:
                    l[j] = i
                    c += 1
                    curr_profit += jobs[i].profit
                    break

        return c, curr_profit

# Time Complexity:
# Greedy (basic): O(n²) → can cause TLE
# Optimized with DSU: O(n log n)
# Space Complexity: O(n) – for tracking time slots