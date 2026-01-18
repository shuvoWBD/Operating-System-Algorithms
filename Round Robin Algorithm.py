# ==================== Round Robin Scheduling ====================

# Input
n = int(input("Enter number of processes: "))
bt = []
rt = []
temp = []

for i in range(n):
    b = int(input(f"Enter burst time of P{i+1}: "))
    bt.append(b)
    rt.append(b)
    temp.append(b)

time_q = int(input("Enter Time Quantum: "))

time = 0
r = n  # remaining processes
wait_time = 0
turn_time = 0
at = 0  # Arrival Time (all assumed 0 for simplicity)

print("\nProcess\tAT\tTAT\tWT\tOrder")

c = 0
while r != 0:
    flag = False
    if rt[c] <= time_q and rt[c] > 0:
        time += rt[c]
        rt[c] = 0
        flag = True
    elif rt[c] > 0:
        rt[c] -= time_q
        time += time_q

    if rt[c] == 0 and flag:
        wt = time - at - bt[c]
        tat = time - at
        r -= 1
        print(f"P{c+1}\t{at}\t{tat}\t{wt}\t{c+1}")
        wait_time += wt
        turn_time += tat
        flag = False

    if c == n-1:
        c = 0
    elif at <= time:
        c += 1
    else:
        c = 0

# ==================== Gantt Chart ====================
print("\n\nGantt Chart\n")
# Top bar
print("\t", end="")
for i in range(time):
    print("--", end="")
print("--")

# Process sequence
print("\t", end="")
j = 0
i = 0
bt_copy = temp.copy()
while i < time:
    if bt_copy[j] >= time_q:
        print(f"P{j+1}    |", end="\t")
        i += time_q
        bt_copy[j] -= time_q
    elif 0 < bt_copy[j] < time_q:
        print(f"P{j+1} |", end="\t")
        i += bt_copy[j]
        bt_copy[j] = 0
    j += 1
    if j >= n:
        j = 0
print()

# Bottom bar
print("\t", end="")
for i in range(time):
    print("--", end="")
print("--")

# Timeline
print("\t0", end="")
j = 0
i = 0
temp_copy = temp.copy()
while i < time:
    if temp_copy[j] >= time_q:
        i += time_q
        print(f"    {i}\t", end="")
        temp_copy[j] -= time_q
    elif 0 < temp_copy[j] < time_q:
        i += temp_copy[j]
        print(f"   {i}\t", end="")
        temp_copy[j] = 0
    j += 1
    if j >= n:
        j = 0

# ==================== Average Times ====================
print(f"\n\nAverage Waiting Time = {wait_time / n:.2f}")
print(f"Average Turnaround Time = {turn_time / n:.2f}")
