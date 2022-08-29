from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count=Counter(students)
        for i in sandwiches:
            if count[i]==0:
                break
            else:
                count[i]-=1
        return count.total()