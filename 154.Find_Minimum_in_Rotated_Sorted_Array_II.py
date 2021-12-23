class Solution:
    def findMin(self, arr: List[int]) -> int:
        low,high=0,len(arr)-1
        if arr[0]<arr[-1]:return arr[0]
        while low<=high:
            if low==high:return arr[low]
            mid=(low+high)//2
            if arr[mid]==arr[low]==arr[high]:high-=1
            elif arr[mid]==arr[high]:high=mid
            elif mid<high and arr[mid]>arr[mid+1]:return arr[mid+1]
            else: low+=1
        return arr[low]
