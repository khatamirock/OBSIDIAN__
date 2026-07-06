
### Ip range

| **Class** | **Range of IPs**           | Ip Addresses             | **Default Subnet Mask**                  | **Hosts per Default Network** | **Purpose**           |
| --------- | -------------------------- | ------------------------ | ---------------------------------------- | ----------------------------- | --------------------- |
| Class A   | 0.0.0.0 to 127.0.0.0       | 0000 0000 - 0111 1111    | 255.0.0.0                                | ~16 million                   | Large organizations   |
| Class B   | 128.0.0.0 to 191.255.0.0   | ==1000== 0000-1011 1111  | 255.255.0.0                              | ~65,534                       | Medium-sized networks |
| Class C   | 192.0.0.0 to 223.255.255.0 | ==1100== 0000- 1101 1111 | 255.255.255.0                            | 254                           | Small networks        |
| Class D   | 224.0.0.0-239.255.255.255  | 1110  0000-  1110  1111  | _Not defined_ (No subnetting in Class D) | Not applicable                | Multicast             |

| Binary Prefix | Range (decimal) | Class / Usage                |
| ------------- | --------------- | ---------------------------- |
| `00000000`    | `0`             | Class A start                |
| `10000000`    | `128`           | Class B start                |
| `11000000`    | `192`           | Class C start                |
| `11100000`    | `224`           | Class D start (Multicast)    |
| `11110000`    | `240`           | Class E start (Experimental) |
| `11111111`    | `255`           | Broadcast (reserved)         |
### **An Example Of Ip Subnetting**:
Sure! Let’s go through an example where we **subnet a larger network into smaller networks**, ensuring each subnet has a fixed number of hosts.
##### [[CDIR & VLSM|see explained example]]
##### [[IP Addressing|examples CIDR..]]

---

#### **Example: Subnetting a Network**

We have a **Class C network: `192.168.10.0/24`**, and we need to divide it into **4 subnets** while ensuring that each subnet supports at least **50 hosts**.

---

##### **Step 1: Identify Required Subnet Mask**

- The **default subnet mask** for `/24` is `255.255.255.0`, allowing **256 total addresses (0-255)**.
- We need **at least 50 hosts per subnet**.
- **Formula for host calculation:** $2^h - 2 \geq \text{Required Hosts}$ where `h` is the number of host bits.

###### **Finding `h`:**

- **2⁶ - 2 = 62 hosts** ✅ (This works, since 2⁵ - 2 = 30 would be too small)
- This means we need **6 bits for hosts**.
- Since an IPv4 address has **32 bits total**, the subnet mask will be: 32−6=26
- New **subnet mask: `/26` (255.255.255.192)**.

---

##### **Step 2: Calculate Subnet Ranges**

Each **/26 subnet** has:

- **Subnet Size:** `2^6 = 64` addresses
- **Usable Hosts:** `62` (since `2` addresses are reserved: **Network Address** & **Broadcast Address**).

Now, let's divide **192.168.10.0/24** into **four /26 subnets**.

###### **Subnet 1 (`192.168.10.0/26`)**

- **Network Address:** `192.168.10.0`  $\to$  -.-.-.==00== 000000
- **Broadcast Address:** `192.168.10.63`   $\to$  -.-.-.==00== 11 1111
- **Usable Host Range:** `192.168.10.1` - `192.168.10.62` 

###### **Subnet 2 (`192.168.10.64/26`)**

- **Network Address:** `192.168.10.64`   $\to$  -.-.-.==01== 00 0000
- **Broadcast Address:** `192.168.10.127`  $\to$  -.-.- ==01== 11 1111
- **Usable Host Range:** `192.168.10.65` - `192.168.10.126`

###### **Subnet 3 (`192.168.10.128/26`)**

- **Network Address:** `192.168.10.128`  $\to$  -.-.-.==10== 00 0000
- **Broadcast Address:** `192.168.10.191`   $\to$  -.-.-. ==10== 11 1111
- **Usable Host Range:** `192.168.10.129` - `192.168.10.190`

###### **Subnet 4 (`192.168.10.192/26`)**

- **Network Address:** `192.168.10.192`   $\to$  -.-.-. ==11== 00 0000
- **Broadcast Address:** `192.168.10.255` $\to$  -.-.-. ==11== 11 1111
- **Usable Host Range:** `192.168.10.193` - `192.168.10.254`

---

##### **Step 3: Summary of the Subnets**

|**Subnet #**|**Network Address**|**Usable Hosts Range**|**Broadcast Address**|
|---|---|---|---|
|**Subnet 1**|192.168.10.0/26|192.168.10.1 - 192.168.10.62|192.168.10.63|
|**Subnet 2**|192.168.10.64/26|192.168.10.65 - 192.168.10.126|192.168.10.127|
|**Subnet 3**|192.168.10.128/26|192.168.10.129 - 192.168.10.190|192.168.10.191|
|**Subnet 4**|192.168.10.192/26|192.168.10.193 - 192.168.10.254|192.168.10.255|

---

##### **Step 4: Verify**

- Each subnet has **64 total addresses**.
- **Usable hosts per subnet:** `62`, meeting our requirement.
- **No overlapping addresses** between subnets.

✅ **Perfect subnetting!** 🚀
 

---
### **Error Detection**:
#### **Primer on Error Detection Techniques**

##### 1. **Simple Parity Check**:

- Adds a single **parity bit** to the data to ensure either:
    
    - **Even parity**: Total number of 1s (data + parity) is even.
    - **Odd parity**: Total number of 1s (data + parity) is odd.
- **Example**:  
    Data = `1011` (4 bits)
    
    - Even parity → Add `0` → Transmitted data: `10110`
    - Odd parity → Add `1` → Transmitted data: `10111`
- **Limitation**: Can detect **single-bit errors** but not multiple-bit errors.
    

---

##### 2. **Two-Dimensional Parity Check**:

- Data is arranged in a **table (block)** format with rows and columns.
    
- Parity bits are added for each **row** and a **column parity** is also calculated.
    
- Helps detect **burst errors** (multiple-bit errors in the same row/column).
    
- **Example**:  
    Data block:
    
    yaml
    
    CopyEdit
    
    `1011 1100 1110`
    
    Add parity bits row-wise and column-wise.
    

---

##### 3. **Cyclic Redundancy Check (CRC)**:

- A more robust error detection technique.
    
- Treats the data as a polynomial and divides it by a predefined **generator polynomial**. The remainder (checksum) is appended to the data.
    
- The receiver performs the same division; if the remainder is non-zero, an error is detected.
    
- **Example**:  
    Data: `11010011101100`  
    Generator polynomial: `1011`  
    CRC appends the remainder (checksum) to the data.
    
- **Advantages**: Can detect **burst errors** and is more reliable than parity checks.
    

---

##### 4. **Checksum**:
^0c3af0

- ==Used in protocols like **TCP/IP**.==
- The sender computes a checksum by adding up all data segments and taking the complement. This is transmitted with the data.
- The receiver performs the same addition and verifies the checksum.
#### 5. **Hamming Code (Error Detection and Correction)** 

- **How it works**: Adds redundant bits to the data using a specific encoding scheme to detect and correct **single-bit errors**. It uses parity concepts for specific bit positions.
- **Strength**: Can both detect and correct errors.
---

##### **Where Are These Used?**

- **Simple and Two-Dimensional Parity**: Low-overhead systems (e.g., small-scale communication systems).
- **CRC**: Used in networking protocols like **Ethernet**, **Wi-Fi**, and **storage devices**.
- **Checksum**: Common in transport protocols like **TCP** and **UDP**.

---


### **What is OSPF?** #star/5 

- OSPF is a **link-state r==outing protocol==** used in IP networks.
- It calculates the ==shortest path== to each destination based on the **Dijkstra algorithm**.
- It divides networks into areas to optimize performance and scalability.
- Routers exchange **link-state advertisements (LSAs)** to maintain a map of the network topology

-**Key Features of OSPF**:
- **Classless Routing**: Supports Variable Length Subnet Masks (VLSM).
- **Cost Metric**: Routing decisions are based on the cost, usually derived from link bandwidth.
- **Convergence**: Faster convergence compared to distance-vector protocols like RIP.
- **Areas**: OSPF uses areas (e.g., backbone area 0) to reduce routing table sizes and improve efficiency.

OSPF v RIP

| Feature      | OSPF                     | RIP                           |
| ------------ | ------------------------ | ----------------------------- |
| Full form    | Open Shortest Path First | Routing Information Protocol  |
| Type         | ==Link state==               | ==Distance vector==               |
| Algorithm    | Dijkstra (SPF)           | Bellman-Ford                  |
| Metric       | Cost (bandwidth-based)   | Hop count                     |
| Max hops     | No fixed limit           | **15 max (16 = unreachable)** |
| Speed        | Fast convergence         | Slow convergence              |
| Updates      | Triggered (only changes) | Periodic (every 30s)          |
| Network size | Large networks           | Small networks                |
| Complexity   | More complex             | Very simple                   |


### OSI Layers (networking layers)

#### **1. Physical Layer**

**Purpose:** Handles the physical connection between devices.  
**Functions:**

- Transmits raw binary data (0s and 1s) as electrical signals, light pulses, or radio waves.
- Defines hardware specifications like cables, switches, and connectors.
- Responsible for data encoding, signal transmission, and synchronization.  
    **Examples:** Ethernet cables, Wi-Fi signals, USB.

---

#### **2. Data Link Layer**

**Purpose:** Ensures ==error-free data transfer between== devices in the same network.  
**Functions:**

- **What Unit:** Organizes data into frames for transmission.
- **What Handels:** Handles error detection and correction (e.g., CRC) and flow control.
- **What Devices:** Manages MAC (Media Access Control) addressing to identify devices.  
    **Examples:** Ethernet (MAC address ==IEEE 802.3==), ==Wi-Fi (802.11), Bluetooth(802.15.1), Wi-Max(802.16)== .
	
---

#### **3. Network Layer**

**Purpose:** Handles routing of data between different networks.  
**Functions:**

- Determines the best path for data using logical addressing (IP addresses).
- Handles congestion control
- Manages packet forwarding and addressing.  
    **Examples:** IP (IPv4/IPv6), routers.

---

#### **4. Transport Layer** [[#^0c3af0|see..]]

**Purpose:** Ensures reliable data transfer between devices ==over the network.==  
**Functions:**

- Segments data into packets and ensures correct sequencing.
- Provides ==error detection, retransmission, and flow control.==
- ==**Port Number initialization**==
- Supports **connection-oriented** (TCP) and **connectionless** (UDP) protocols.  
    **Examples:** TCP, UDP.
	**TCP -** Three-Way Handshake: Before data is sent, TCP establishes a connection using a three-step handshake (SYN, SYN-ACK, ACK) to synchronize communication.

---

#### **5. Session Layer**

**Purpose:** Manages sessions between applications on different devices.  
**Functions:**

- Establishes, maintains, and terminates communication sessions.
- Handles session recovery after interruptions.  
    **Examples:** Remote desktop, file transfer sessions.

---

#### **6. Presentation Layer**

**Purpose:** Translates data into a format understood by the application layer.  
**Functions:**

- Handles data encryption, compression, and translation.
- Ensures proper data syntax and semantics.  
    **Examples:** SSL/TLS encryption, JPEG, ASCII.

---

#### **7. Application Layer**

**Purpose:** Interfaces with end-user applications and provides network services.  
**Functions:**

- Supports user applications like browsers, email clients, and file sharing.
- Handles application-specific protocols.  
    **Examples:** HTTP, FTP, SMTP, DNS.

---

[[networking Table and others Algos..|see Algo & Tables & networking devices work..]]
#### **Summary** of OSI layer

| Place | **Layer**                                                              | **Data Unit** | **Examples**                                                              | **Function**                                                                                                                                                                                                                                         |
| ----- | ---------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7     | **Application**                                                        | Data          | HTTP, FTP, DNS                                                            | User interface and network services                                                                                                                                                                                                                  |
| 6     | **Presentation**                                                       | Data          | SSL/TLS, **JPEG**(comprsn), ASCII                                         | Data translation, encryption, compression                                                                                                                                                                                                            |
| 5     | **Session**                                                            | Data          | APIs, session control                                                     | Session management                                                                                                                                                                                                                                   |
| 4     | **Transport**<br>[[TCP to Ensure Reliable\| ⭐why TCP is reliable ???]] | Segments      | TCP, UDP,<br>==Port numbers >> (**thats why is works for application**==) | - Reliable delivery, <br>- **End-to-End communication** between ==applications==, **retransmission**<br>- error handling, **Error checking (Parity), and flow control**.<br><br>-convt. ==data into **segments**== before passing it to Layer 3.<br> |
| 3     | **Network**                                                            | Packets       | IP, ICMP(ping), routers                                                   | logical Routing and addressing<br>-Splits ==segments into **packets**==                                                                                                                                                                              |
| 2     | **Data Link**                                                          | Frames        | ==**Ethernet**==, MAC address<br>==(end to End)==                         | - Ensures **error-free** transmission<br>- Detects **physical transmission errors** (e.g., electrical noise) between two **directly connected devices** (Hop-to-Hop)<br>- converts  ==**packets (from Layer 3) into frames**==                       |
| 1     | **Physical**                                                           | Bits          | Cables, Wi-Fi                                                             | Raw data transmission                                                                                                                                                                                                                                |

> ==**SPF...B**  $\to$ Segment  $\to$ Packet $\to$ Frame==     <<<<<<<<<<<<<<<<<<<

Each layer builds upon the next to enable seamless communication across networks.
##### **DIFF between TCP & UDP**: 
- **TCP (Transmission Control Protocol) → Reliable communication**
    - Ensures data arrives in **order and without errors**.
    - Uses **handshaking (SYN, SYN-ACK, ACK)** to establish a connection.
    - If data is lost, it will **retransmit** it.
- **UDP (User Datagram Protocol) → Fast but unreliable communication**
    - Sends data ==**without checking if it arrives correctly**.==
    - Used for **live streaming, gaming, and VoIP**, where speed matters more than reliability.

| Feature        | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| -------------- | ----------------------------------- | ---------------------------- |
| Type           | Connection-oriented                 | Connectionless               |
| Reliability    | ✅ Reliable (guarantees delivery)    | ❌ Unreliable                 |
| Data Order     | ✅ Maintains order                   | ❌ No guarantee               |
| Error Checking | ✅ Yes (with retransmission)         | ⚠️ Basic only                |
| Speed          | Slower                              | Faster                       |
| Acknowledgment | ✅ Uses ACKs                         | ❌ No ACK                     |
| Flow Control   | ✅ Yes                               | ❌ No                         |
| Overhead       | High                                | Low                          |

#### **Trnasport Layer vs Data Link Layer — The Core Difference**

| Feature               | **Transport Layer (L4)**                               | **Data Link Layer (L2)**                                |
| --------------------- | ------------------------------------------------------ | ------------------------------------------------------- |
| **Scope**             | End-to-End (between two computers across the internet) | Node-to-Node (between two directly connected devices)   |
| **Address Used**      | **Port numbers** (e.g., TCP port 80 for HTTP)          | **MAC addresses** (hardware addresses)                  |
| **Reliability**       | Ensures complete, ordered delivery of _messages_       | Ensures error-free delivery of _frames_ across one link |
| **Unit of Data**      | **Segment (TCP)** / **Datagram (UDP)**                 | **Frame**                                               |
| **Error Handling**    | End-to-end checks (TCP ACKs, retransmission)           | Local checks (Frame Check Sequence, CRC)                |
| **Example Protocols** | TCP, UDP                                               | Ethernet (802.3), PPP, Wi-Fi (802.11)                   |
| **Works Between**     | Processes (apps on different computers)                | Network interfaces (NICs or switches)                   |
| **Flow Control**      | Controls how much data one computer sends              | Controls how fast frames move over one link             |
##### 🧠 **One-Line Memory Hook**

> 🔹 **Transport = End-to-End (Software → Software)**  
> 🔹 **Data Link = Node-to-Node (Hardware → Hardware)**



--- 
### **Digital Technology** #Digital_Techn
##### **Correct Answer:**
 
1. **NRZ (Non-Return-to-Zero)**
    
    - **NRZ-L (Level)**: 0 and 1 are represented by different voltage levels.
    - **NRZ-I (Invert on 1)**: Voltage only changes when a **1** occurs.
2. **RZ (Return-to-Zero)**
    
    - Each bit returns to zero before the next bit starts (unlike NRZ).
3. **Manchester Encoding**
    
    - A **0** is represented as **high-to-low** transition, and **1** as **low-to-high** transition within a single bit period.
4. **AMI (Alternate Mark Inversion)**
    
    - **0 is represented by zero voltage**, and **1 is alternately positive and negative**.

If you can provide the actual line coding waveform or characteristics, I can confirm the correct answer.

---

#### **Difference Between Wireless Ad-hoc and Wireless (Infrastructure) Networks**

| Feature               | **Wireless Ad-hoc Network**                                                                                           | **Wireless (Infrastructure) Network**                                                                        |
| --------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Definition**        | A ==decentralized== wireless network where devices ==communicate directly== without a central router or access point. | A structured wireless network where devices connect through a central access point (router or base station). |
| **Topology**          | Peer-to-peer (P2P), no fixed infrastructure.                                                                          | Client-server, requires an access point.                                                                     |
| **Setup**             | Easy and quick to set up; no external devices needed.                                                                 | Requires a Wi-Fi router or AP for communication.                                                             |
| **Scalability**       | ==Limited scalability==; performance degrades with more nodes.                                                        | ==More scalable;== supports many devices efficiently.                                                        |
| **Reliability**       | Less reliable due to potential interference and dynamic topology changes.                                             | More reliable because of centralized management and stable connections.                                      |
| **Example Use Cases** | Military, disaster recovery, ==temporary network==s (conferences, gaming).                                            | ==Home Wi-Fi,== corporate networks, public hotspots.                                                         |




21. Difference between Divide and Conquer and 
	**1. Divide and Conquer (D&C)**
	
	🔹 **Breaks a problem into smaller subproblems, ==solves them independently==, and combines the results.**
	
	#### **Key Features:**
	
	- The subproblems are usually ==**completely independent**==.
	- Uses **recursion** to break the problem into smaller parts.
	- The results of subproblems are ==**not reused**.==
	- Works well when the same subproblem is **not solved multiple times**.
	- **Time Complexity**: Often **O(n log n) or worse** due to repeated computation.
	
	#### **Examples of D&C:** **Merge Sort** (Splits an array into halves, sorts each half, then merges)
	
	
	**Dynamic Programming (DP)**
	🔹 **Breaks a problem into overlapping subproblems, solves each subproblem once, and stores the ==results for reuse.**==
	
	#### **Key Features:**
	
	- The subproblems **overlap**, meaning they are solved multiple times.
	- **Memoization (Top-Down Approach)** or **Tabulation (Bottom-Up Approach)** is used to avoid redundant calculations.
	- Saves time by storing solutions to subproblems and reusing them.
	- **Time Complexity**: Often **O(n) or O(n²)** (better than naive recursion).




22. ad
23. asd
24. 