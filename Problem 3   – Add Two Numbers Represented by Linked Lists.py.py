# cook your dish here
import sys

def add_linked_lists():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # Parse the first linked list (length n and its elements)
    n = int(input_data[0])
    list1 = [int(x) for x in input_data[1:n+1]]
    
    # Parse the second linked list (length m and its elements)
    m_idx = n + 1
    m = int(input_data[m_idx])
    list2 = [int(x) for x in input_data[m_idx+1 : m_idx+1+m]]
    
    result = []
    carry = 0
    i, j = 0, 0
    
    # Process digit by digit until both lists are exhausted and no carry remains
    while i < n or j < m or carry > 0:
        val1 = list1[i] if i < n else 0
        val2 = list2[j] if j < m else 0
        
        total = val1 + val2 + carry
        
        # Append the unit digit of the sum to the result
        result.append(total % 10)
        
        # Calculate the carry for the next position
        carry = total // 10
        
        i += 1
        j += 1
        
    # Print the resulting digits separated by a space
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    add_linked_lists()