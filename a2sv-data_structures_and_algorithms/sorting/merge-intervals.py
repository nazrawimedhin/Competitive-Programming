class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        iters = len(intervals) - 1
        for i in range(iters):
            length = len(intervals) -1
            if i < length:
                check_one = intervals[i]
                check_two = intervals[i+1]
                if check_one[0] < check_two[0] and check_one[1] > check_two[1]:
                    intervals.pop(i+1)
                    continue
                elif check_one[0] > check_two[0] and check_one[1] < check_two[1]:
                    intervals.pop(i)
                    continue
                elif check_one[0] == check_two[0] and check_one[1] == check_two[1]:
                    intervals.pop(i+1)
                    continue
                elif check_one[0] < check_two[0] and check_one[1] < check_two[1] and check_one[1] > check_two[0]:
                    intervals[i] = [check_one[0], check_two[1]]
                    intervals.pop(i+1)
                    continue
                elif check_one[0] > check_two[0] and check_one[1] > check_two[1] and check_one[0] < check_two[1]:
                    intervals[i] = [check_two[0], check_one[1]]
                    intervals.pop(i+1)
                    continue
                elif check_one[0] == check_two[0] and check_one[1] < check_two[1]:
                    intervals[i] = check_two
                    intervals.pop(i)
                    continue
                elif check_one[0] == check_two[0] and check_one[1] > check_two[1]:
                    intervals[i] = check_one
                    intervals.pop(i+1)
                    continue
                elif check_one[0] < check_two[0] and check_one[1] == check_two[1]:
                    intervals[i] = check_one
                    intervals.pop(i+1)
                    continue
                elif check_one[0] > check_two[0] and check_one[1] == check_two[1]:
                    intervals[i] = check_two
                    intervals.pop(i)
                    continue
                elif check_one[1] == check_two[0]:
                    intervals[i] = [check_one[0], check_two[1]]
                    intervals.pop(i+1)
                    continue
                elif check_one[0] == check_two[1]:
                    intervals[i] = [check_two[0], check_one[1]]
                    intervals.pop(i+1)
                    continue
            else:
                break
        return intervals
