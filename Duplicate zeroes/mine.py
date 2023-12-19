class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        queue = collections.deque()
        i = 0
        while i < len(arr):
            if arr[i] != 0:
                if len(queue) > 0:
                    if len(queue) <= abs((i+1) - len(arr)):
                        queue.append(arr[i])
                    replace_with = queue.popleft()
                    arr[i] = replace_with
            else:
                if len(queue) > 0:
                    if len(queue) <= abs((i+1) - len(arr)):
                        queue.append(0)
                        queue.append(0)
                    replace_with = queue.popleft()
                    arr[i] = replace_with
                else:
                    queue.append(0)
            i = i+1
        
