class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        p1 = 0
        p2 = len(people)-1
        boats = 0

        while p1<=p2:
            if p1 == p2:
                boats += 1
                break
            
            wt = people[p2] + people[p1]
            if wt > limit:
                boats += 1
                p2 -= 1
            else:
                boats += 1
                p1+=1
                p2-=1
        return boats



        