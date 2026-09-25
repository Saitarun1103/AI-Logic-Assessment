# cook your dish here
import sys
from collections import deque

def longest_stable_window():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    # Extract exactly n signal values
    nums = [int(x) for x in input_data[1:n+1]]
    k = int(input_data[n+1])
    
    left = 0
    max_len = 0
    best_start = 1
    
    # Deques to store indices for the maximum and minimum values in the window
    min_dq = deque()
    max_dq = deque()
    
    for right in range(n):
        val = nums[right]
        
        # Maintain max_dq: keep indices in decreasing order of their values
        while max_dq and nums[max_dq[-1]] <= val:
            max_dq.pop()
        max_dq.append(right)
        
        # Maintain min_dq: keep indices in increasing order of their values
        while min_dq and nums[min_dq[-1]] >= val:
            min_dq.pop()
        min_dq.append(right)
        
        # If the window is invalid (difference exceeds k), shrink it from the left
        while nums[max_dq[0]] - nums[min_dq[0]] > k:
            left += 1
            # Remove indices that have fallen out of the current window
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()
                
        # Calculate current valid window length
        current_len = right - left + 1
        
        # Update max_len and best_start if a strictly longer window is found
        if current_len > max_len:
            max_len = current_len
            best_start = left + 1  # 1-based indexing
            
    print(f"{max_len} {best_start}")

if __name__ == "__main__":
    longest_stable_window()