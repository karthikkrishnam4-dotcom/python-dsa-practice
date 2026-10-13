class Solution:
    def intervels_at(self,intervels):
        intervels.sort(key=lambda intervel:intervel[1])
        last_end=float("-inf")
        count=0
        for start,end in intervels:
            if start>=last_end:
                last_end=end
            else:
                count+=1
        return count
intervels = [[1, 2], [1, 3], [2, 3], [3, 4]]

solution = Solution()
print(solution.intervels_at(intervels))