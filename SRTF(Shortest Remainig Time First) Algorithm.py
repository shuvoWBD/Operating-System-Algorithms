# ==================== SRTF Scheduling (Python 3) ====================

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0
        self.rt = 0
        self.start_time = -1

# ============ Input ============
n = int(input("Enter total number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Process {i} Arrival Time: "))
    bt = int(input(f"Enter Process {i} Burst Time: "))
    processes.append(Process(i, at, bt))

# ============ Initialization ============
bt_remaining = [p.bt for p in processes]
is_completed = [False] * n
is_first_process = True
current_time = 0
completed = 0
sum_tat = 0
sum_wt = 0
sum_rt = 0
total_idle_time = 0
prev = 0

# ============ SRTF Scheduling ============
while completed != n:
    min_index = -1
    minimum = float('inf')

    for i in range(n):
        if processes[i].at <= current_time and not is_completed[i]:
            if bt_remaining[i] < minimum:
                minimum = bt_remaining[i]
                min_index = i
            elif bt_remaining[i] == minimum:
                if processes[i].at < processes[min_index].at:
                    min_index = i

    if min_index == -1:
        current_time += 1
    else:
        # First time execution
        if bt_remaining[min_index] == processes[min_index].bt:
            processes[min_index].start_time = current_time
            total_idle_time += 0 if is_first_process else (processes[min_index].start_time - prev)
            is_first_process = False

        bt_remaining[min_index] -= 1
        current_time += 1
        prev = current_time

        if bt_remaining[min_index] == 0:
            processes[min_index].ct = current_time
            processes[min_index].tat = processes[min_index].ct - processes[min_index].at
            processes[min_index].wt = processes[min_index].tat - processes[min_index].bt
            processes[min_index].rt = processes[min_index].start_time - processes[min_index].at

            sum_tat += processes[min_index].tat
            sum_wt += processes[min_index].wt
            sum_rt += processes[min_index].rt

            completed += 1
            is_completed[min_index] = True

# ============ Metrics ============
max_completion_time = max(p.ct for p in processes)
min_arrival_time = min(p.at for p in processes)
length_cycle = max_completion_time - min_arrival_time

cpu_utilization = (length_cycle - total_idle_time) / length_cycle

# ============ Output ============
print("\nProcess No.\tAT\tBT\tCT\tTAT\tWT\tRT")
for p in processes:
    print(f"{p.pid}\t\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}\t{p.rt}")

print(f"\nAverage Turn Around Time = {sum_tat/n:.2f}")
print(f"Average Waiting Time     = {sum_wt/n:.2f}")
print(f"Average Response Time    = {sum_rt/n:.2f}")
print(f"Throughput               = {n/length_cycle:.2f}")
print(f"CPU Utilization(%)       = {cpu_utilization*100:.2f}")
