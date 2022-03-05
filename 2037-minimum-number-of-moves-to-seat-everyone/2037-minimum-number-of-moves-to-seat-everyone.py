class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        a=[]
        for i in range(len(seats)):
            b=abs(students[i]-seats[i])
            a.append(b)
        return (sum(a))
        