# Input reading
n, l = map(int, input().split())
potholes = [list(map(int, input().split())) for _ in range(n)]

# Sort potholes by starting point
potholes.sort()

# Initialize variables
current_end = 0
planks_needed = 0

# Process each pothole
for start, end in potholes:
    if current_end >= end:
        # Already covered this pothole
        continue
    
    # If the current end is less than the start of the pothole, start from the beginning of the pothole
    start = max(start, current_end)
    
    # Calculate how many planks are needed for this pothole
    num_planks = (end - start + l - 1) // l  # Ceiling division to ensure full coverage
    
    # Update the end position of the last placed plank
    current_end = start + num_planks * l
    
    # Increment the total number of planks used
    planks_needed += num_planks

# Output the result
print(planks_needed)
