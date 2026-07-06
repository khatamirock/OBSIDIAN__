### Scheduling
[[Operating System (OS)#**3. CPU Scheduling Algorithms**|see all.....]]
#### **Shortest Job First (SJF) Scheduling How It Works**:
Processes are executed in order of their **shortest estimated burst time**.
- **Practicality**:
    - While SJF minimizes average waiting time and is theoretically optimal, it is **highly improbable** to implement because:
        - **Exact burst time (process duration) is ==unknown in advance.**==
        - Requires **prediction mechanisms**, which are error-prone.
        - Dynamic workloads make this impractical in many real-world scenarios.
    - ==Variants like== **Shortest Remaining Time First (SRTF)** or approximations using heuristics are more realistic.
- **Improbability**: **Highly improbable** due to reliance on perfect knowledge of process durations.



#### **Scheduling Algorithms.**
##### **SRTF (==Preemptive== SJF) Scheduling Example**

##### **Process Details**  
| Process | Arrival Time (AT) | Burst Time |
| ------- | ----------------- | ---------- |
| P1      | 0                 | 8          |
| P2      | 1                 | 4          |
| P3      | 2                 | 2          |
| P4      | 3                 | 1          |
| P5      | 4                 | 3          |
| P6      | 5                 | 2          |

---

##### **Gantt Chart**  
![[Pasted image 20250124225445.png]]
```
| P1 (0–1) | P2 (1–2) | P3 (2–4) | P4 (4–5) | P6 (5–7) | P2 (7–10) | P5 (10–13) | P1 (13–20) |
```

---

##### **Calculations**  
| Process | CT (completion time) (depends on the gnatt chart  ) | Arrival Time (AT) | TAT = CT - AT | Burst Time | WT = TAT - Burst | RT (response time) First Execution−AT |
| ------- | --------------------------------------------------- | ----------------- | ------------- | ---------- | ---------------- | ------------------------------------- |
| P1      | 20                                                  | 0                 | 20 - 0 = 20   | 8          | 20 - 8 = 12      | 0                                     |
| P2      | 10                                                  | 1                 | 10 - 1 = 9    | 4          | 9 - 4 = 5        | 1                                     |
| P3      | 4                                                   | 2                 | 4 - 2 = 2     | 2          | 2 - 2 = 0        | 2                                     |
| P4      | 5                                                   | 3                 | 5 - 3 = 2     | 1          | 2 - 1 = 1        | 4                                     |
| P5      | 13                                                  | 4                 | 13 - 4 = 9    | 3          | 9 - 3 = 6        | 10                                    |
| P6      | 7                                                   | 5                 | 7 - 5 = 2     | 2          | 2 - 2 = 0        | 5                                     |

---

##### **Average Times**  
- **Average Turnaround Time (TAT)**:$$
 ( \frac{20 + 9 + 2 + 2 + 9 + 2}{6} = \frac{44}{6} \approx 7.33 )  
$$
- **Average Waiting Time (WT)**: 
$$
( \frac{12 + 5 + 0 + 1 + 6 + 0}{6} = \frac{24}{6} = 4.0 )  
$$
- **Average Response Time (RT)**: 
$$
( \frac{0 + 1 + 2 + 4 + 10 + 5}{6} = \frac{22}{6} \approx 3.67 )  
$$

---

###### **Key Takeaways**  
1. **SRTF (Preemptive SJF)** minimizes waiting time by prioritizing the shortest remaining burst time.  
2. **Preemption** occurs when a ==new/old  process with a shorter burst time arrives.==  



#### **Round Robin Scheduling Example**

##### **Process Details**  
| Process | Arrival Time (AT) | Burst Time (BT) |     |
| ------- | ----------------- | --------------- | --- |
| P1      | 0                 | 5               |     |
| P2      | 1                 | 3               |     |
| P3      | 2                 | 1               |     |
| P4      | 3                 | 2               |     |
| P5      | 4                 | 3               |     |

**Time Quantum = 2 units**  

---

##### **Gantt Chart**  
```
| P1 (0–2) | P2 (2–4) | P3 (4–5) | P4 (5–7) | P5 (7–9) | P1 (9–11) | P2 (11–12) | P5 (12–13) | P1 (13–14) |  
```

---

##### **Calculations**  
| Process | Arrival Time (AT) | CT  | TAT = CT - AT | WT = TAT - BT |
| ------- | ----------------- | --- | ------------- | ------------- |
| P1      | 0                 | 14  | 14 - 0 = 14   | 14 - 5 = 9    |
| P2      | 1                 | 12  | 12 - 1 = 11   | 11 - 3 = 8    |
| P3      | 2                 | 5   | 5 - 2 = 3     | 3 - 1 = 2     |
| P4      | 3                 | 7   | 7 - 3 = 4     | 4 - 2 = 2     |
| P5      | 4                 | 13  | 13 - 4 = 9    | 9 - 3 = 6     |

---

##### **Average Times**  
- **Average Waiting Time (WT)**:  
$$
  \frac{9 + 8 + 2 + 2 + 6}{5} = \frac{27}{5} = 5.4 \text{ units}
$$
- **Average Turnaround Time (TAT)**:  
  
$$
  \frac{14 + 11 + 3 + 4 + 9}{5} = \frac{41}{5} = 8.2 \text{ units}
$$   
##### **Key Steps Explained**  
1. **P1** runs first (0–2), remaining BT = 3.  
2. **P2** runs (2–4), remaining BT = 1.  
3. **P3** runs (4–5), finishes (BT=1).  
4. **P4** runs (5–7), finishes (BT=2).  
5. **P5** runs (7–9), remaining BT = 1.  
6. **P1** runs again (9–11), remaining BT = 1.  
7. **P2** resumes (11–12), finishes.  
8. **P5** resumes (12–13), finishes.  
9. **P1** finishes (13–14).  




#### **==Preemptive== Priority Scheduling Example**

##### **Assumed Process Details**  
| Process | Arrival Time (AT) | Priority (Higher = Better) | Burst Time (BT) |  
|---------|-------------------|----------------------------|-----------------|  
| P1      | 0                 | 2                          | 4               |  
| P2      | 1                 | 3                          | 1               |  
| P3      | 2                 | 4                          | 2               |  
| P4      | 3                 | 5                          | 1               |  
| P5      | 4                 | 5                          | 3               |  

**Mode**: Preemptive (higher priority interrupts lower priority).  

---

##### **Gantt Chart**  
```
| P1 (0–1) | P2 (1–2) | P3 (2–3) | P4 (3–4) | P5 (4–7) | P3 (7–8) | P1 (8–11) |  
```

---

##### **Calculations**  
| Process | CT  | TAT = CT - AT | WT = TAT - BT |  
|---------|-----|---------------|----------------|  
| P1      | 11  | 11 - 0 = 11   | 11 - 4 = 7     |  
| P2      | 2   | 2 - 1 = 1     | 1 - 1 = 0      |  
| P3      | 8   | 8 - 2 = 6     | 6 - 2 = 4      |  
| P4      | 4   | 4 - 3 = 1     | 1 - 1 = 0      |  
| P5      | 7   | 7 - 4 = 3     | 3 - 3 = 0      |  

---

##### **Average Times**  
- **Average Waiting Time (WT)**:  
  
  $\frac{7 + 0 + 4 + 0 + 0}{5} = \frac{11}{5} = 2.2 \text{ units}$
  
- **Average Turnaround Time (TAT)**:  
  
  $\frac{11 + 1 + 6 + 1 + 3}{5} = \frac{22}{5} = 4.4 \text{ units}$
  

---

###### **Key Steps Explained**  
1. **Time 0–1**: P1 (priority 2) runs.  
2. **Time 1**: P2 (priority 3) arrives and preempts P1.  
3. **Time 1–2**: P2 runs to completion.  
4. **Time 2**: P3 (priority 4) arrives and preempts P1.  
5. **Time 2–3**: P3 runs.  
6. **Time 3**: P4 (priority 5) arrives and preempts P3.  
7. **Time 3–4**: P4 runs to completion.  
8. **Time 4**: P5 (priority 5) arrives. Since P4 is done, P5 runs.  
9. **Time 4–7**: P5 runs to completion.  
10. **Time 7–8**: Resume P3 (remaining BT=1).  
11. **Time 8–11**: Resume P1 (remaining BT=3).  

---

 
### **Page Replacement Algorithms:**
#### 1. Optimal Page Replacement Algorithm
- ==we will find which item in current memory is furthest to be used !!== those will be **==replaced==**

![[Optimal Page Replacement Algorithm-full.png]]
- here for the first miss, ee can see that `1` has no or very little use in the `near future`, so we will replace that with current demand of cpu
- similarly for the next miss for `4` er can see that `2` has the ==farthest from near use== or demand, so we Will replace that


#### 2. LRU -Least Recently Used
- this is completely ==reverse== of optimal replacement algorithm
- what we find here is the resource cpu used in the ==earliest of its demand== or (that cpu reffered in the most early among the current frame)
- 
![[LRU.png]]

- here to replace 5 we will see that among the available frame in memory which ==was the earliest that the cpu needed==
- and we can see that 3 is the number, so we will replace `3` with `1`
- for 4 the earliest need was `1` so we replace that with `4`

---
ANOTHER : Let’s use the reference string:

  **7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2**
 
|Step|Reference|Frames (after)|Status|Replacement Reason|
|:-:|:-:|---|:-:|---|
|1|7|[7, -, -]|Miss|(Empty; load 7)|
|2|0|[7, 0, -]|Miss|(Empty; load 0)|
|3|1|[7, 0, 1]|Miss|(Empty; load 1)|
|4|2|[2, 0, 1]|Miss|Replace 7 (least recently used: step 1)|
|5|0|[2, 0, 1]|**Hit**|0 is already present|
|6|3|[2, 0, 3]|Miss|Replace 1 (last used at step 3)|
|7|0|[2, 0, 3]|**Hit**|0 is present|
|8|4|[4, 0, 3]|Miss|Replace 2 (last used at step 4)|
|9|2|[4, 0, 2]|Miss|Replace 3 (last used at step 6)|
|10|3|[4, 3, 2]|Miss|Replace 0 (last used at step 7)|
|11|0|[0, 3, 2]|Miss|Replace 4 (last used at step 8)|
|12|3|[0, 3, 2]|**Hit**|3 is present|
|13|2|[0, 3, 2]|**Hit**|2 is present|

**Counting faults and hits:**

- **Page Faults (Misses):** Steps 1, 2, 3, 4, 6, 8, 9, 10, 11 → 9 faults
- **Hits:** Steps 5, 7, 12, 13 → 4 hits

Thus, for 13 page references:

- **Hit Ratio:** 4⁄13 ≈ 30.8%
- **Miss Ratio:** 9⁄13 ≈ 69.2%
 
#### Step 3. Average Memory Access Time (“Waiting Time”)

Although page‐replacement algorithms aren’t usually measured by “waiting time,” we can compute an average memory access time (AMAT) if we assume:

- A **hit** costs 1 ms,
- A **miss** (page fault) costs 8 ms.

Then:

  **AMAT = (Hit Ratio × 1 ms) + (Miss Ratio × 8 ms)**

Using our ratios:

- Hit ratio ≈ 0.308 and miss ratio ≈ 0.692, so

  AMAT ≈ 0.308 × 1 + 0.692 × 8  
      ≈ 0.308 + 5.536  
      ≈ 5.844 ms

Thus, the average access (or “waiting”) time is approximately 5.84 ms.

---

#### Summary of the Example

- **Reference String:** 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
- **Frames:** 3
- **Page Faults:** 9 (Miss Ratio ≈ 69.2%)
- **Hits:** 4 (Hit Ratio ≈ 30.8%)
- **Average Memory Access Time (Assuming hit = 1 ms, fault = 8 ms):** ~5.84 ms

This example (with the accompanying table and timeline “Gantt chart”) illustrates the LRU page replacement algorithm along with the derived hit/miss ratios and an estimated average access time.



## **State Diagram**


![[State Diagram.png]]


 
## **🔹 Process Management Cheat Sheet**

#### **1️⃣ Process Basics**

- **Process** → A running instance of a program.
- **States of a Process:**
    - **New** → Process is created.
    - **Ready** → Waiting to be assigned CPU.
    - **Running** → Executing on CPU.
    - **Blocked (Waiting)** → Waiting for I/O or resource.
    - **Terminated** → Process has finished execution.

**🔹 Process Control Block (PCB)** → Stores process info like PID, state, registers, memory, etc.

---

#### **2️⃣ Process Scheduling**

- **Long-Term Scheduler (Job Scheduler):**
    - Selects which processes enter the ==**Ready Queue**.==
    - Controls the degree of **multiprogramming**.
- **Short-Term Scheduler (CPU Scheduler):**
    - Decides which process gets CPU **next**.
    - Works at **millisecond-level**.
- **Medium-Term Scheduler:**
    - **Swaps** processes in and out of memory to control CPU load.

---

#### **3️⃣ CPU Scheduling Algorithms**[[#**Scheduling**|Meths..]]

|Algorithm|Preemptive?|Characteristics|
|---|---|---|
|**FCFS (First Come First Serve)**|❌ No|Simple but can cause long waiting times.|
|**SJF (Shortest Job First)**|✅ (SRTF) / ❌ (Non-preemptive)|Optimal for lowest avg. wait time but **can cause starvation**.|
|**Round Robin (RR)**|✅ Yes|Time-sharing, fair for all processes. Uses a **time quantum**.|
|**Priority Scheduling**|✅ / ❌|Higher priority runs first, **can cause starvation**.|
|**Multilevel Queue (MLQ)**|✅ Yes|Processes divided into multiple queues (Foreground, Background, etc.).|
|**Multilevel Feedback Queue (MLFQ)**|✅ Yes|Processes can move between queues based on behavior.|

💡 **Starvation Fix:** ==Use **Aging**== (increase priority of long-waiting processes).

---

#### **4️⃣ Process Synchronization**

**🔹 Race Condition** → Multiple processes access shared resources simultaneously, causing unexpected results.  
**🔹 Critical Section** → Code that accesses shared resources.  
**🔹 Mutual Exclusion** → Ensures only one process accesses the critical section at a time.

**🔹 Solutions to ==Synchronization Problems:**==

- **Mutex (Mutual Exclusion Lock)** → ==Only one process== can enter critical section.
- **Semaphore** (Two Types):
    - **Binary Semaphore (0 or 1)** → Works like a mutex.
    - **Counting Semaphore (0 to N)** → ==Allows multiple processes.==
- **Monitor** → High-level abstraction that controls access to resources.

**Common Problems:**

| **Problem**    | **Description**                                                       | **Solution**                                                             |
| -------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Deadlock**   | Two or more processes wait for each other indefinitely.               | ==A==voidance (==B==anker's Algorithm), Prevention, Detection & Recovery |
| **Starvation** | A process waits indefinitely because others always preempt resources. | Aging (Increase priority over time)                                      |

---

#### **5️⃣ Deadlocks**

**🔹 Conditions for Deadlock (Coffman’s Conditions)** → ==If all 4 happen==, deadlock occurs:  
Got it! Here are the **4 necessary conditions for deadlock** explained in very simple terms:

---

##### 1. **Mutual Exclusion**

Only one process can use a resource at a time.  
	_Example:_ If one process is using a printer, no other process can use it at the same time.

##### 2. **Hold and Wait**

A process is holding one resource and waiting for another.  
	_Example:_ A process is using the printer and waiting for the scanner.
>You’re holding the hostel bathroom key but also waiting for the shower towel someone else is using.
##### 3. **No Preemption**

You can't take resources away from a process; it must give them up willingly.  
	_Example:_ If a process is using the printer, you can’t force it to stop using it—you have to wait.
> If someone has the towel, you can’t snatch it; you must wait until they return it.

##### 4. **Circular Wait**
Processes are waiting on each other in a circle.  
_Example:_
- Process A waits for a resource held by Process B,
- Process B waits for one held by Process C,
- and Process C waits for one held by Process A.

---

Would you like these as flashcards or want them turned into a diagram?

**🔹 Deadlock Prevention Strategies:**  
✅ **Break any one of the 4 conditions** (e.g., prevent circular wait by ordering resource allocation).  
✅ **Deadlock Avoidance:** **Banker's Algorithm** (allocates resources only if it keeps the system safe).

---

#### **6️⃣ Interprocess Communication (IPC)**

**🔹 Why IPC?** → Allows processes to communicate & share data.

| **IPC Mechanism**   | **Description**                                          |
| ------------------- | -------------------------------------------------------- |
| **Shared Memory**   | Fast but needs synchronization (e.g., using semaphores). |
| **Message Passing** | Uses `send()` & `receive()` system calls.                |
| **Pipes**           | Unidirectional data flow between processes.              |
| **Sockets**         | Used for communication ==over network==s.                |

---

#### **7️⃣ Memory Management (Brief Overview)**

| **Concept**        | **Description**                                             |
| ------------------ | ----------------------------------------------------------- |
| **Paging**         | Divides memory into ==fixed-size== **pages**.               |
| **Segmentation**   | Divides memory into ==variable-sized== segments.            |
| **Virtual Memory** | Uses disk as extra RAM (via swapping).                      |
| **Thrashing**      | ==Too much swapping== between RAM & disk slows performance. |

---

#### **8️⃣ Exam Quick Tricks**

✔ **If a process waits indefinitely → It’s starvation.**  
✔ **If processes are waiting for each other → It’s deadlock.**  
✔ **If the system is swapping too much → It’s thrashing.**   (==caused by page Fault==) 
✔ **If it asks about “optimal” scheduling → SJF (Shortest Job First).**  
✔ **If there’s “fairness” → Round Robin (RR) is best.**  
✔ **If priority scheduling causes issues → Apply Aging to prevent starvation.**

---

##### **💡 Super Fast Revision**

📌 **Processes** → States: New, Ready, Running, Waiting, Terminated.  
📌 **Scheduling** → FCFS, SJF, RR, Priority, MLFQ.  
📌 **Deadlocks** → 4 Conditions (Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait).  
📌 **Synchronization** → Mutex, Semaphore, Monitor.  
📌 **IPC** → Shared Memory, Message Passing, Pipes, Sockets.
 