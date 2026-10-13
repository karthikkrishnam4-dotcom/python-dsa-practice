class Solution:
    def meeting(self,start,end):
        meetings=list(zip(start,end))
        meetings.sort(key=lambda meeting:meeting[1])
        count=0
        last_end=float("-inf")
        for meeting_start,meeting_end in meetings:
            if meeting_start>last_end:
                last_end=meeting_end
                count+=1
        return count
start = [1, 3, 0, 5, 8, 5]
end =   [2, 4, 6, 7, 9, 9]

solution = Solution()
print(solution.meeting(start, end))