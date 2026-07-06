# Practice Questions from Study Materials

## Question 1: Algorithm Complexity & Sorting

**Which of the following sorting algorithms has a worst-case time complexity of O(n²) but is optimal for average case waiting time in CPU scheduling?**

a) Merge Sort  
b) Quick Sort  
c) Shortest Job First (SJF)  
d) Heap Sort

**Answer:** c) Shortest Job First (SJF)

**Explanation:** SJF is a CPU scheduling algorithm (not a sorting algorithm), but it uses the concept of selecting the process with the smallest burst time. While Quick Sort has O(n²) worst case, SJF is specifically mentioned in the OS notes as being optimal for average waiting time, though it requires knowledge of future burst times.

---

## Question 2: Data Structures - Binary Trees

**Given a binary tree with height h, what is the maximum number of nodes possible?**

a) 2^h  
b) 2^(h+1) - 1  
c) h^2  
d) 2^h - 1

**Answer:** b) 2^(h+1) - 1

**Explanation:** According to the Data Structures notes, the maximum number of nodes in a tree of height h is 2^(h+1) - 1. This represents a perfect binary tree where all levels are completely filled.

---

## Question 3: Operating Systems - Process States

**A process cannot directly transition from which state to the Running state?**

a) Ready  
b) Waiting (Blocked)  
c) New  
d) Both b and c

**Answer:** d) Both b and c

**Explanation:** According to the OS notes, a process in the Waiting state must first transition to Ready before it can go to Running. A process in the New state also cannot directly go to Running - it must first go to Ready. Only Ready → Running is a direct transition.

---

## Question 4: Database - Normalization

**Which normal form eliminates transitive dependencies?**

a) 1NF  
b) 2NF  
c) 3NF  
d) BCNF

**Answer:** c) 3NF

**Explanation:** According to the Database notes, Third Normal Form (3NF) ensures that a table is in 2NF and eliminates transitive dependencies, where a non-prime attribute depends on another non-prime attribute rather than directly on the primary key.

---

## Question 5: Networking - OSI Model

**At which layer of the OSI model does a Router operate?**

a) Layer 1 (Physical)  
b) Layer 2 (Data Link)  
c) Layer 3 (Network)  
d) Layer 4 (Transport)

**Answer:** c) Layer 3 (Network)

**Explanation:** According to the Networking notes, a Router operates at Layer 3 (Network Layer) and makes forwarding decisions based on IP addresses. It breaks up broadcast domains.

---

## Question 6: Memory Management - Paging

**Which type of fragmentation does Paging suffer from?**

a) External Fragmentation  
b) Internal Fragmentation  
c) Both  
d) Neither

**Answer:** b) Internal Fragmentation

**Explanation:** According to the OS notes, Paging divides logical memory into fixed-size pages and physical memory into fixed-size frames. It suffers from Internal Fragmentation (unused space within a page), while Segmentation suffers from External Fragmentation.

---

## Question 7: Algorithms - Graph Traversal

**Which algorithm uses a Queue data structure for traversal?**

a) Depth-First Search (DFS)  
b) Breadth-First Search (BFS)  
c) Both  
d) Neither

**Answer:** b) Breadth-First Search (BFS)

**Explanation:** According to the Data Structures notes, BFS uses a Queue to explore level by level, while DFS uses a Stack (or recursion) to explore as deeply as possible before backtracking.

---

## Question 8: Database - ER Diagrams

**For a Many-to-Many (M:N) relationship between two entities, what is the minimum number of tables required?**

a) 1  
b) 2  
c) 3  
d) 4

**Answer:** c) 3

**Explanation:** According to the Database notes, M:N relationships always require 3 tables: one for each entity and a third relationship table (junction table) to map the many-to-many relationship.

---

## Question 9: Operating Systems - Deadlock

**Which of the following is NOT one of the four necessary conditions for deadlock?**

a) Mutual Exclusion  
b) Hold and Wait  
c) Preemption  
d) Circular Wait

**Answer:** c) Preemption

**Explanation:** According to the OS notes, the four necessary conditions are: 1) Mutual Exclusion, 2) Hold and Wait, 3) **No Preemption** (not Preemption), and 4) Circular Wait. The condition states that resources cannot be forcibly taken away.

---

## Question 10: Data Structures - Heap

**What is the time complexity of building a heap from an array of n elements?**

a) O(n log n)  
b) O(n)  
c) O(log n)  
d) O(n²)

**Answer:** b) O(n)

**Explanation:** According to the Data Structures notes, building a heap from an array in one go (heapify) is O(n), not O(n log n). This is a common exam trick question.

---

## Question 11: Networking - TCP

**How many steps are involved in the TCP 3-way handshake for connection establishment?**

a) 2  
b) 3  
c) 4  
d) 5

**Answer:** b) 3

**Explanation:** According to the CSE notes, the TCP 3-way handshake involves: 1) SYN (Client sends connection request), 2) SYN-ACK (Server responds), 3) ACK (Client confirms connection).

---

## Question 12: Database - SQL

**Which SQL command category includes CREATE, ALTER, and DROP?**

a) DML (Data Manipulation Language)  
b) DDL (Data Definition Language)  
c) DCL (Data Control Language)  
d) TCL (Transaction Control Language)

**Answer:** b) DDL (Data Definition Language)

**Explanation:** According to the Database notes, DDL commands (DR. CAT: DROP, RENAME, CREATE, ALTER, TRUNCATE) are used to define and modify database structure.

---

## Question 13: Operating Systems - Scheduling

**Which CPU scheduling algorithm can lead to starvation of low-priority processes?**

a) FCFS (First-Come-First-Served)  
b) Round Robin  
c) Priority Scheduling  
d) Shortest Job First

**Answer:** c) Priority Scheduling

**Explanation:** According to the OS notes, Priority Scheduling can lead to starvation of low-priority processes. The solution is Aging, which increases priority over time.

---

## Question 14: Data Structures - Sorting Stability

**Which of the following sorting algorithms is NOT stable?**

a) Merge Sort  
b) Insertion Sort  
c) Selection Sort  
d) Radix Sort

**Answer:** c) Selection Sort

**Explanation:** According to the Data Structures notes, Selection Sort, Quick Sort, and Heap Sort are NOT stable. Merge Sort, Insertion Sort, and Radix Sort are stable.

---

## Question 15: Networking - IP Addressing

**What is the default subnet mask for a Class C network?**

a) 255.0.0.0  
b) 255.255.0.0  
c) 255.255.255.0  
d) 255.255.255.255

**Answer:** c) 255.255.255.0

**Explanation:** According to the Networking notes, Class C networks (192.0.0.0 to 223.255.255.0) have a default subnet mask of 255.255.255.0.

---

## Question 16: Database - Functional Dependencies

**In functional dependency X → Y, what is X called?**

a) Dependent  
b) Determinant  
c) Candidate Key  
d) Super Key

**Answer:** b) Determinant

**Explanation:** According to the Database notes, in a functional dependency X → Y, X is the Determinant (the attribute that determines the value) and Y is the Dependent.

---

## Question 17: Operating Systems - Memory Management

**Which page replacement algorithm suffers from Belady's Anomaly?**

a) FIFO  
b) LRU  
c) Optimal  
d) All of the above

**Answer:** a) FIFO

**Explanation:** According to the OS notes, Belady's Anomaly occurs when increasing the number of frames can increase the number of page faults. This only happens with FIFO page replacement algorithm.

---

## Question 18: Data Structures - Graph Representation

**For a sparse graph, which representation is more space-efficient?**

a) Adjacency Matrix  
b) Adjacency List  
c) Both are equal  
d) Depends on the graph

**Answer:** b) Adjacency List

**Explanation:** According to the Data Structures notes, Adjacency List has space complexity O(V+E) which is better for sparse graphs, while Adjacency Matrix has O(V²) which is better for dense graphs.

---

## Question 19: Networking - Collision Domains

**Which device breaks up collision domains?**

a) Hub  
b) Switch  
c) Router  
d) Repeater

**Answer:** b) Switch

**Explanation:** According to the Networking notes, a Switch operates at Layer 2 and breaks up collision domains (one per port), while a Hub creates one large collision domain. A Router breaks up broadcast domains.

---

## Question 20: Database - Keys

**What is the relationship between Super Key, Candidate Key, and Primary Key?**

a) Super Key → Candidate Key → Primary Key  
b) Primary Key → Candidate Key → Super Key  
c) They are independent  
d) Candidate Key → Super Key → Primary Key

**Answer:** a) Super Key → Candidate Key → Primary Key

**Explanation:** According to the Database notes, Super Key is the broadest (any set that uniquely identifies), Candidate Key is a minimal Super Key (no redundant attributes), and Primary Key is the chosen Candidate Key. Each is chosen from the upper layer.

---

## Question 21: Operating Systems - Semaphores

**What does the P() operation do in semaphore terminology?**

a) Increments the semaphore value  
b) Decrements the semaphore value  
c) Sets the semaphore to 1  
d) Sets the semaphore to 0

**Answer:** b) Decrements the semaphore value

**Explanation:** According to the OS notes, P() or wait() decrements the semaphore value. If the value becomes negative, the process blocks. V() or signal() increments the semaphore value.

---

## Question 22: Data Structures - Binary Search Tree

**What does an in-order traversal of a Binary Search Tree yield?**

a) Random order  
b) Pre-order sequence  
c) Sorted sequence  
d) Post-order sequence

**Answer:** c) Sorted sequence

**Explanation:** According to the Data Structures notes, an in-order traversal (LNR: Left → Node → Right) of a BST yields a sorted sequence because of the BST property: all keys in left subtree < node's key < all keys in right subtree.

---

## Question 23: Networking - TCP vs UDP

**Which protocol is connection-oriented?**

a) TCP  
b) UDP  
c) Both  
d) Neither

**Answer:** a) TCP

**Explanation:** According to the CSE notes, TCP is connection-oriented (like a phone call - requires connection setup), while UDP is connectionless (like sending a postcard - no setup needed).

---

## Question 24: Database - Views

**Which of the following is true about a View in a database?**

a) It stores actual data  
b) It only stores the SQL query definition  
c) It is always faster than a table  
d) It cannot be modified

**Answer:** b) It only stores the SQL query definition

**Explanation:** According to the Database notes, a View is a virtual table that does not store data, only the SQL query definition. Data is retrieved dynamically from underlying tables when accessed.

---

## Question 25: Operating Systems - File Allocation

**Which file allocation method provides the fastest sequential access?**

a) Contiguous  
b) Linked  
c) Indexed  
d) All are equal

**Answer:** a) Contiguous

**Explanation:** According to the OS notes, Contiguous allocation stores file blocks in consecutive order on disk, providing very fast sequential access. However, it suffers from external fragmentation.

---

## Question 26: Data Structures - Heap Property

**In a Max-Heap, what is the relationship between a parent and its children?**

a) Parent's key ≤ children's keys  
b) Parent's key ≥ children's keys  
c) Parent's key = children's keys  
d) No specific relationship

**Answer:** b) Parent's key ≥ children's keys

**Explanation:** According to the Data Structures notes, a Max-Heap satisfies the property that the parent's key is greater than or equal to the children's keys. For a Min-Heap, it's the opposite (parent's key ≤ children's keys).

---

## Question 27: Networking - NAT

**What is the primary purpose of NAT (Network Address Translation)?**

a) To increase network speed  
b) To allow multiple devices to share a single public IP address  
c) To encrypt network traffic  
d) To prevent viruses

**Answer:** b) To allow multiple devices to share a single public IP address

**Explanation:** According to the CSE notes, NAT allows multiple devices on a local network to share a single public IP address, helping conserve IPv4 addresses and providing security by hiding internal IP addresses.

---

## Question 28: Database - RAID

**Which RAID level uses striping without parity for maximum performance?**

a) RAID-0  
b) RAID-1  
c) RAID-5  
d) RAID-10

**Answer:** a) RAID-0

**Explanation:** According to the Database notes, RAID-0 uses striping (data split across disks) without parity, providing the fastest performance but no redundancy. It has no fault tolerance.

---

## Question 29: Operating Systems - Process Schedulers

**Which scheduler controls the degree of multiprogramming?**

a) Short-Term Scheduler  
b) Medium-Term Scheduler  
c) Long-Term Scheduler  
d) All of them

**Answer:** c) Long-Term Scheduler

**Explanation:** According to the OS notes, the Long-Term Scheduler (Job Scheduler) selects processes from the job pool and loads them into memory, controlling the degree of multiprogramming.

---

## Question 30: Data Structures - Hash Tables

**Which collision resolution technique uses linked lists at each table index?**

a) Linear Probing  
b) Quadratic Probing  
c) Double Hashing  
d) Chaining

**Answer:** d) Chaining

**Explanation:** According to the Data Structures notes, Chaining (Open Hashing) resolves collisions by having each table index point to a linked list of keys that hash to that index. The other options are forms of Open Addressing (Closed Hashing).

---

## Answer Key Summary

1. c) Shortest Job First (SJF)
2. b) 2^(h+1) - 1
3. d) Both b and c
4. c) 3NF
5. c) Layer 3 (Network)
6. b) Internal Fragmentation
7. b) Breadth-First Search (BFS)
8. c) 3
9. c) Preemption
10. b) O(n)
11. b) 3
12. b) DDL
13. c) Priority Scheduling
14. c) Selection Sort
15. c) 255.255.255.0
16. b) Determinant
17. a) FIFO
18. b) Adjacency List
19. b) Switch
20. a) Super Key → Candidate Key → Primary Key
21. b) Decrements the semaphore value
22. c) Sorted sequence
23. a) TCP
24. b) It only stores the SQL query definition
25. a) Contiguous
26. b) Parent's key ≥ children's keys
27. b) To allow multiple devices to share a single public IP address
28. a) RAID-0
29. c) Long-Term Scheduler
30. d) Chaining
