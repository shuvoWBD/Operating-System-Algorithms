# Operating-System-Algorithms

Operating system scheduling and resource management algorithms decide the execution order of processes and allocation of resources to ensure efficiency and fairness. FCFS, SRTF, Priority, and Round Robin focus on CPU scheduling based on arrival, burst time, or priority, while Banker’s Algorithm prevents deadlocks by maintaining a safe state. Together, these algorithms optimize system performance, minimize waiting time, and ensure safe and orderly process execution.


**Algorithms Included**
-----------------------------------
**First Come First Serve (FCFS) Scheduling Algorithm**

* Processes are executed in the order of their arrival time.

* Non-preemptive: once a process starts, it runs to completion.

* Simple and easy to implement using a queue.

* Waiting time can be high if a long process arrives first (convoy effect).

* Commonly used in batch systems and basic CPU scheduling.

  


**Shortest Remaining Time First (SRTF) Scheduling Algorithm**

* Preemptive version of Shortest Job Next (SJN) scheduling.

* CPU always executes the process with the smallest remaining burst time.

* Can interrupt a running process if a shorter job arrives.

* Minimizes average waiting and turnaround time compared to FCFS.

* Suitable for time-sharing systems where quick response is needed.



**Priority Scheduling Algorithm**

* Each process is assigned a priority, and the CPU executes the highest-priority process first.

* Can be preemptive or non-preemptive depending on implementation.

* Lower-priority processes may suffer from starvation if higher-priority processes keep arriving.

* Can use aging technique to gradually increase the priority of waiting processes.

* Useful when some tasks need to be completed before others based on importance.



**Round Robin Algorithm**

* Each process is assigned a fixed time quantum and executed in a cyclic order.

* Preemptive: a process is interrupted when its time quantum expires.

* Ensures fair CPU allocation among all processes.

* Suitable for time-sharing systems to provide good response time.

* Average waiting time depends on the choice of the time quantum.



**Banker’s Algorithm**

Used for deadlock avoidance in operating systems.

Allocates resources only if the system remains in a safe state.

Considers maximum demand, allocation, and available resources for each process.

Checks for a sequence of processes that can finish without causing deadlock.

Useful in systems with multiple instances of each resource type.
