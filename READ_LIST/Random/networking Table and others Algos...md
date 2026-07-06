## 🔹 1. Tables used in Networking (WHERE & WHY)

|**Table Name**|**Layer**|**Device**|**Used For**|
|---|---|---|---|
|**Routing Table**|Network (L3)|Router|Decides best path to destination|
|**Forwarding Table (FIB)**|Network (L3)|Router|Fast packet forwarding|
|**NAT Table**|Network (L3)|Router/Gateway|Maps private IP ↔ public IP|
|**ARP Table**|Network ↔ Data Link|Host/Router|IP → MAC mapping|
|**MAC Address Table**|Data Link (L2)|Switch|MAC → port mapping|
|**CAM Table**|Data Link (L2)|Switch|Hardware MAC table|
|**DNS Cache**|Application|Host/DNS Server|Domain → IP mapping|
|**TCP Connection Table**|Transport (L4)|Host|Tracks TCP sessions|
|**Firewall Rule Table**|L3–L4|Firewall|Allow / block traffic|

---

## 🔹 2. Algorithms used in Networking (WHERE)

### 📍 Routing Algorithms

| **Algorithm** | **Layer** | **Used In**           | **Protocol** |
| ------------- | --------- | --------------------- | ------------ |
| Dijkstra      | Network   | Shortest path         | OSPF         |
| Bellman–Ford  | Network   | Distance vector       | RIP          |
| SPF           | Network   | Link-state routing    | OSPF         |
| Path Vector   | Network   | Inter-network routing | BGP          |

---

### 📍 Error Detection & Control Algorithms

|**Algorithm**|**Layer**|**Purpose**|
|---|---|---|
|CRC|Data Link|Error detection|
|Checksum|Transport|Error detection|
|ARQ|Data Link|Error recovery|
|Sliding Window|Data Link / Transport|Flow + error control|

---

### 📍 Congestion & Flow Control

|**Algorithm / Mechanism**|**Layer**|
|---|---|
|TCP Slow Start|Transport|
|AIMD|Transport|
|Flow Control|Transport|
|Congestion Control|Transport|

---

## 🔹 3. Addressing used in each Layer

|**Layer**|**Address Type**|**Example**|
|---|---|---|
|Application|Name|www.google.com|
|Transport|Port|80, 443|
|Network|IP|192.168.1.1|
|Data Link|MAC|00:1A:2B:3C|
|Physical|Bits|0s and 1s|

---

## 🔹 4. Devices & their Working Layer 

| **Device**               | **Layer** | **Key Work**        |
| ------------------------ | --------- | ------------------- |
| Hub, Repeater            | Physical  | Broadcast bits      |
| Switch, Bridge           | Data Link | Uses MAC table      |
| Router, (Layer 3 Switch) | Network   | Uses routing table  |
| Gateway                  | L3–L7     | Protocol conversion |
| Firewall                 | L3–L4     | Packet filtering    |

---

## 🔹 5. Protocols used in each Layer

| **Layer**   | **Protocols**        |
| ----------- | -------------------- |
| Application | HTTP, FTP, SMTP, DNS |
| Transport   | TCP, UDP             |
| Network     | IP, ICMP, NAT        |
| Data Link   | ARP, Ethernet        |
| Physical    | Cables, signals      |

---

## 🔹 6. NAT, ARP, DNS (VERY EXAM-IMPORTANT)

|**Concept**|**Layer**|**Uses Table?**|
|---|---|---|
|NAT|Network|NAT Table|
|ARP|Network ↔ L2|ARP Table|
|DNS|Application|DNS Cache|

---

## 🔹 7. One-line Memory Trick 🧠

> **Switch → MAC table → L2**  
> **Router → Routing + NAT table → L3**  
> **TCP → Ports + Sliding Window → L4**