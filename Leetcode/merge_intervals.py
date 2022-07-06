"""def mergei(intervals):
    for i in range(len(intervals)-1):
            if(intervals[i][0]<=intervals[i+1][0]):
                if(intervals[i][1]<=intervals[i+1][1]):
                    intervals.remove(intervals[i])

    return intervals"""

def mergei(intervals):
    for i in range(len(intervals)-1):
        if(intervals[i][0]<=intervals[i+1][0]) and (intervals[i][1]<=intervals[i+1][1]):
            print(intervals[i+1][0])    

    return intervals




intervals = [[1,3],[2,6],[8,10],[15,18]]

print(mergei(intervals))