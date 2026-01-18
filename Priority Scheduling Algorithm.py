# ================== Priority Scheduling (Non-Preemptive) ==================

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Input number of processes
n = int(input("Enter Number of Processes: "))

burst = []
priority = []
index = []

# Input burst time and priority
for i in range(n):
    while True:
        try:
            b, p = map(int, input(f"Enter Burst Time and Priority Value for Process {i+1} (e.g. 5 2): ").split())
            break
        except ValueError:
            print("Invalid input! Enter two integers separated by space.")
    burst.append(b)
    priority.append(p)
    index.append(i + 1)

# Sort processes by priority (higher value = higher priority)
for i in range(n):
    max_idx = i
    for j in range(i, n):
        if priority[j] > priority[max_idx]:
            max_idx = j
    swap(priority, i, max_idx)
    swap(burst, i, max_idx)
    swap(index, i, max_idx)

# Execution order
t = 0
print("\nOrder of process Execution:")
for i in range(n):
    print(f"P{index[i]} is executed from {t} to {t + burst[i]}")
    t += burst[i]

# Calculate waiting times
print("\nProcess Id\tBurst Time\tWait Time")
wait_time = 0
total_wait_time = 0

for i in range(n):
    print(f"P{index[i]}\t\t{burst[i]}\t\t{wait_time}")
    total_wait_time += wait_time
    wait_time += burst[i]

avg_wait_time = total_wait_time / n
print(f"\nAverage Waiting Time: {avg_wait_time:.2f}")

# Calculate turnaround times
turnaround_times = [burst[i] + (total_wait_time if i == n-1 else sum(burst[:i])) for i in range(n)]
total_turnaround = sum([burst[i] + sum(burst[:i]) for i in range(n)])
avg_turnaround = total_turnaround / n

print(f"Average Turnaround Time: {avg_turnaround:.2f}")
