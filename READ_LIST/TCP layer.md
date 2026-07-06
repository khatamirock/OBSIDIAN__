The **7 layers of the OSI** (Open Systems Interconnection) model** describe how data travels from one device to another across a network. Each layer has specific tasks and communicates with the layer directly above or below it.

---

### **1. Physical Layer**

**Purpose:** Handles the physical connection between devices.  
**Functions:**

- Transmits raw binary data (0s and 1s) as electrical signals, light pulses, or radio waves.
- Defines hardware specifications like cables, switches, and connectors.
- Responsible for data encoding, signal transmission, and synchronization.  
    **Examples:** Ethernet cables, Wi-Fi signals, USB.

---

### **2. Data Link Layer**

**Purpose:** Ensures error-free data transfer between devices in ==the same network.==  
**Functions:**

- Organizes data into frames for transmission.
- Handles error detection and correction (e.g., CRC).
- Manages ==MAC== (Media Access Control) addressing to identify devices.  
    **Examples:** Ethernet (MAC address), Wi-Fi (802.11).

---

### **3. Network Layer**

**Purpose:** Handles routing of data ==between different networks.==  
**Functions:**

- Determines ==the best path for data using logical addressing (IP addresses).==   <<<<<<<<< **LOGICAL ADDRESSING**
- Manages packet forwarding and addressing.  
    **Examples:** IP (IPv4/IPv6), routers.

---

### **4. Transport Layer**

**Purpose:** Ensures reliable data transfer between devices.  
**Functions:**

- Segments data into packets and ensures correct sequencing.
- Provides error detection, retransmission, and flow control.
- Supports connection-oriented (==TCP==) and connectionless (==UDP==) ==protocols==.  
    **Examples:** TCP, UDP.

---

### **5. Session Layer**

**Purpose:** Manages sessions between applications on different devices.  
**Functions:**

- Establishes, maintains, and terminates communication sessions.
- Handles session recovery after interruptions.  
    **Examples:** Remote desktop, file transfer sessions.

---

### **6. Presentation Layer**

**Purpose:** Translates data into a format understood by the application layer.  
**Functions:**

- Handles data encryption, compression, and translation.
- Ensures proper data syntax and semantics.  
    **Examples:** SSL/TLS encryption, JPEG, ASCII.

---

### **7. Application Layer**

**Purpose:** Interfaces with end-user applications and provides network services.  
**Functions:**

- Supports user applications like browsers, email clients, and file sharing.
- Handles application-specific protocols.  
    **Examples:** HTTP, FTP, SMTP, DNS.

---

### **Summary**

| **Layer**        | **Data Unit** | **Examples**          | **Function**                                  |
| ---------------- | ------------- | --------------------- | --------------------------------------------- |
| **Application**  | Data          | HTTP, FTP, DNS        | User interface and network services           |
| **Presentation** | Data          | SSL/TLS, JPEG, ASCII  | Data translation, ==encryption==, compression |
| **Session**      | Data          | APIs, session control | Session management                            |
| **Transport**    | Segments      | TCP, UDP              | Reliable delivery, error handling             |
| **Network**      | Packets       | IP, ICMP, routers     | Routing and addressing - (IP Addr)            |
| **Data Link**    | Frames        | Ethernet, MAC address | Error-free data transmission - (MAC)          |
| **Physical**     | Bits          | Cables, Wi-Fi         | Raw data transmission                         |

