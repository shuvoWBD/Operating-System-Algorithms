# ==================== Banker's Algorithm (Python 3) ====================

# Number of processes and resources
n = 5
m = 3

# Allocation Matrix
alloc = [
    [0, 1, 0],  # P0
    [2, 0, 0],  # P1
    [3, 0, 2],  # P2
    [2, 1, 1],  # P3
    [0, 0, 2],  # P4
]

# MAX Matrix
max_matrix = [
    [7, 5, 3],  # P0
    [3, 2, 2],  # P1
    [9, 0, 2],  # P2
    [2, 2, 2],  # P3
    [4, 3, 3],  # P4
]

# Available Resources
avail = [3, 3, 2]

# Finish flags and safe sequence
f = [0] * n
ans = []

# Calculate Need Matrix
need = [[max_matrix[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

# Banker’s Algorithm
for _ in range(n):
    allocated = False
    for i in range(n):
        if f[i] == 0:
            if all(need[i][j] <= avail[j] for j in range(m)):
                # Can allocate
                ans.append(i)
                for j in range(m):
                    avail[j] += alloc[i][j]
                f[i] = 1
                allocated = True
    if not allocated:
        break  # No allocation possible, unsafe state

# Check if system is safe
if all(f[i] == 1 for i in range(n)):
    print("Following is the SAFE Sequence:")
    print(" -> ".join(f"P{p}" for p in ans))
else:
    print("The system is not safe")
