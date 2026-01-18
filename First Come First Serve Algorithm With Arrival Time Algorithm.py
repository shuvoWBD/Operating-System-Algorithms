def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


n = int(input("Enter Number of Processes: "))

burst = []
priority = []
index = []

for i in range(n):
    b, p = map(int, input(
        f"Enter Burst Time and Priority Value for Process {i + 1}: "
    ).split())
    burst.append(b)
    priority.append(p)
    index.append(i + 1)

# Sorting processes based on priority (higher value = higher priority)
for i in range(n):
    max_idx = i
    for j in range(i, n):
        if priority[j] > priority[max_idx]:
            max_idx = j

    swap(priority, i, max_idx)
    swap(burst, i, max_idx)
    swap(index, i, max_idx)

t = 0
print("\nOrder of process Execution is")
for i in range(n):
    print(f"P{index[i]} is executed from {t} to {t + burst[i]}")
    t += burst[i]

print("\nProcess Id\tBurst Time\tWait Time")
wait_time = 0
total_wait_time = 0

for i in range(n):
    print(f"P{index[i]}\t\t{burst[i]}\t\t{wait_time}")
    total_wait_time += wait_time
    wait_time += burst[i]

avg_wait_time = total_wait_time / n
print(f"\nAverage waiting time is {avg_wait_time}")

total_turnaround = sum(burst)
avg_turnaround = total_turnaround / n
print(f"Average TurnAround Time is {avg_turnaround}")
