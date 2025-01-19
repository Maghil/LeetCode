class Solution:
    def minimumChairs(self, actions: str) -> int:
        total_chair, free_chair, min_chair = 0,0, 0
        for action in actions:
            if action == "E":
                if free_chair>0:
                    free_chair-=1
                else:
                    total_chair+=1
            else:
                free_chair+=1
            if free_chair==0 and min_chair < total_chair:
                min_chair = total_chair
        return min_chair