from MinHeap import MinHeap
from MaxHeap import MaxHeap

# Challenge 1: Convert Max-Heap to Min-Heap
def convertMax(maxHeap):
    if not maxHeap or len(maxHeap) <= 0:
        return None

    # O(n) find min
    root = min(maxHeap)
    minHeap = [root]
    for node in maxHeap:
        if node != root:
            minHeap.append(node)
    return minHeap

# Challenge 2: Find K Smallest Elements using a minHeap 
def findKSmallest(lst, k):
    minHeap = MinHeap()
    minHeap.buildHeap(lst)
    min_k = []
    for i in range(k):
        min_k.append(minHeap.removeMin())
    return min_k

# Challenge 3: Find K Largest Elements using a maxHeap 
def findKLargest(lst, k):
    maxHeap = MaxHeap()
    maxHeap.buildHeap(lst)
    max_k = []
    for i in range(k):
        max_k.append(maxHeap.removeMax())
    return max_k

# Challenge 3: Sldiding Window Median
class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    result = []
    # median = middle val
    # sliding window to get all sulists of k elements -> sort each sublist, get middle val, add to median array
    # Each time we sort we shift winow only one index, therefore just need to insert its value at relevant position
    start_index = 0
    end_index = k-1
    # while we haven't reached the end of the list
    while end_index < len(nums):
        sub = nums[start_index:end_index]
        # sort the first subarray
        if start_index == 0:
            sub.sort()
        else:
            # All elements in the array except for the last are sorted...
            # We just need an O(n) operation to position this element in the sub
            # We will continue swapping the final value with the next value in the array until it is in the correct spot
            final = sub[len(sub)-1]
            # Correct spot
            index = 0
            while sub[index] < final:
                index += 1
            # Correct spot for last element of sub was found
            # insert element at index
            sub.insert(index-1, final)
            # remove final element as we've re-added in the correct position
            sub = sub[0:len(sub)-1]
        # Add the median of the subarray to the result list
        result.append(sub[k/2])
        start_index+=1
        end_index+=1
    return result

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


