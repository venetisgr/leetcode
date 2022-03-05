class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         #Method 1 Sorting
        
#         # sort list and find the kth element
#         #sorting complexity is O(n *logn)
        
#         ret = nums.copy()
#         ret = sorted(ret)
        
#         return ret[-k]

#         #Method 2  Heap 
            
#         #https://stackoverflow.com/a/68164713
        
#         #python only has min heap so we need to multiply erverything with -1 to get max heap  O(N)
#         # Heapify, constructing a heap from an existing list takes O(N)
#         #pushing the maximum element takes O(logn)
#         #We need to push until we reach the kth largest -> O (k *log(N))

#         #Total complexity  O(k *log(N)) + 2*O(N) -> O(k *log(N)
        
#         from heapq import heapify, heappop
        
#         heap = [element * -1 for element in nums] # python only has min heap so we need to multiply erverything with -1 to get max heap 
#         #heapq.heapify(heap)
#         heapify(heap) #heapify
#         #print(nums)
#         #print(list(heap))
        
#         ret = None
#         for i in range(k):
#             #push k elements
#             ret = heappop(heap)
    
#         return ret*-1

#         #Method 3 Heap

#         import heapq
    
#         #Built in method #O(N * logk) time and 0(K) space  (in reality it is k+ (N * logk), first k has to do with heapify)
        
#         return heapq.nlargest(k, nums)[-1] #returns kth largest from biggest to smallest k, we want the kth one
        
    
        #Method 4 K element min heap #similar to the built in mentioned above
        
        # If we have k element min heap, the top element will be the smallest, so from the k elements in heap we would have the kth smallest element in the top of
        #the heap
        
        # If we push another element we will have a k+1 heap, but from those elements we want the k largest ones so we will drop the k+1 element which is the 
        #smallest one and is  in the top of the heap. This will lead to a heap with k elements again where the kth one/ top one is the kth largest so far. 
        
        #So we have to do this N times, for pushing an element the complexity is 0(logK) and for popping one it is 0(logK)
        #O( N*log(K) )
        
        import heapq
        
        heap = nums[:k] # we will start with a heap of k elements
        heapq.heapify(heap) #convert a list to a heap O(k)
        
        for number in nums[k:]: #push the rest of the numbers
            heapq.heappush(heap,number) #k +1 heap 
            heapq.heappop(heap) #k heap, the kth one is the  kth largest one
            
        return  heapq.heappop(heap)
        
