# cook your dish here
import sys

def consolidate_time_slots():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Parse the intervals
    intervals = []
    idx = 1
    for _ in range(n):
        start = int(input_data[idx])
        end = int(input_data[idx+1])
        intervals.append([start, end])
        idx += 2
        
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    # Merge overlapping intervals
    merged = []
    for interval in intervals:
        # If the merged list is empty or there is no overlap, append the current interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Overlap exists, update the end time of the last merged interval
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    # Print the final consolidated intervals
    for start, end in merged:
        print(f"{start} {end}")

if __name__ == "__main__":
    consolidate_time_slots()