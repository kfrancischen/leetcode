# meeting room 1: whether can meet
def canAttendMeeting(nums):
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i][0] <= nums[i-1][1]:
            return False


    return True


# meeting room 2: how many room needed
import heapq
def minMeetingRooms(nums):
    nums = sorted(nums)
    heap = []
    numOfRoom = 0
    for i in range(len(nums)):
        if not heap:
            heapq.heappush(heap, nums[i][1])
            numOfRoom += 1
            continue
        if heap[0] <= nums[i][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i][1])
        else:
            heapq.heappush(heap, nums[i][1])
            numOfRoom += 1

    return numOfRoom

nums = [[1,2],[5,6],[3,4]]
print canAttendMeeting(nums)
print minMeetingRooms(nums)
nums.append([2,4])
print canAttendMeeting(nums)
print minMeetingRooms(nums)
