class Solution:
    def job_schedule(self,jobs):
        jobs.sort(key=lambda job:job[2],reverse=True)
        maximum_deadline=min(max(job[1] for job in jobs),len(jobs))
        slots=[None]*(maximum_deadline+1)
        schedule_time=0
        total_profit=0
        for name,deadline,profit in jobs:
            for slot in range(min(deadline,maximum_deadline),0,-1):
                if slots[slot]==None:
                    slots[slot]=name
                    schedule_time+=1
                    total_profit+=profit
                    break
        return schedule_time,total_profit
jobs = [
    ["A", 2, 100],
    ["B", 1, 50],
    ["C", 2, 20]
]
solution = Solution()
answer = solution.job_schedule(jobs)

print(answer)