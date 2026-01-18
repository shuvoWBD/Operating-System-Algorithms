class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0


def print_table(processes):
    print("+-----+------------+--------------+-----------------+")
    print("| PID | Burst Time | Waiting Time | Turnaround Time |")
    print("+-----+------------+--------------+-----------------+")
    for p in processes:
        print(f"| {p.pid:2d}  |     {p.burst_time:2d}     |"
              f"      {p.waiting_time:2d}      |"
              f"        {p.turnaround_time:2d}       |")
        print("+-----+------------+--------------+-----------------+")


def print_gantt_chart(processes):
    # top bar
    print(" ", end="")
    for p in processes:
        print("--" * p.burst_time, end=" ")
    print()

    # process ids
    print("|", end="")
    for p in processes:
        print(" " * (p.burst_time - 1), end="")
        print(f"P{p.pid}", end="")
        print(" " * (p.burst_time - 1), end="")
        print("|", end="")
    print()

    # bottom bar
    print(" ", end="")
    for p in processes:
        print("--" * p.burst_time, end=" ")
    print()

    # timeline
    current_time = 0
    print(f"{current_time}", end="")
    for p in processes:
        space = 2 * p.burst_time
        current_time += p.burst_time
        print(" " * (space - len(str(current_time))), end="")
        print(f"{current_time}", end="")
    print("\n")


# ================= MAIN =================

n = int(input("Enter total number of process: "))
processes = []

print("Enter burst time for each process:")
for i in range(n):
    bt = int(input(f"P[{i + 1}] : "))
    processes.append(Process(i + 1, bt))

# calculate waiting time & turnaround time
processes[0].turnaround_time = processes[0].burst_time

for i in range(1, n):
    processes[i].waiting_time = (
        processes[i - 1].waiting_time + processes[i - 1].burst_time
    )
    processes[i].turnaround_time = (
        processes[i].waiting_time + processes[i].burst_time
    )

# total & average calculations
total_waiting_time = sum(p.waiting_time for p in processes)
total_turnaround_time = sum(p.turnaround_time for p in processes)

print()
print_table(processes)

print(f"\nTotal Waiting Time      : {total_waiting_time}")
print(f"Average Waiting Time    : {total_waiting_time / n:.2f}")
print(f"Total Turnaround Time   : {total_turnaround_time}")
print(f"Average Turnaround Time : {total_turnaround_time / n:.2f}")

print("\n          GANTT CHART          ")
print("          ***********          ")
print_gantt_chart(processes)
