#User function Template for python3

class Solution: 
    def select(self, arr, i):
        current_small = i
        for j in range(i+1, len(arr)):
            if arr[current_small] > arr[j]:
                current_small = j
        return current_small
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
            current_small = self.select(arr, i)
            if current_small != i:
                temp = arr[current_small]
                arr[current_small] = arr[i]
                arr[i] = temp

# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends
