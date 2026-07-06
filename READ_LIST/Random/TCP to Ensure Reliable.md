
# ✍️ **Functions of TCP to Ensure Reliable Communication**

👉  
TCP provides reliability over an unreliable network by performing the following functions:

---

## ✅ **1. Sequence Numbering**

👉 Each byte/segment is assigned a **sequence number**

- Ensures **correct order of data**
    
- Helps detect **missing or duplicate packets**
    

---

## 📩 **2. Acknowledgment (ACK)**

👉 Receiver sends acknowledgment for received data

- Confirms successful delivery
    
- Sender knows what has been received
    

---

## 🔁 **3. Retransmission**

👉 If ACK is not received within a time → data is retransmitted

- Handles **lost packets**
    

---

## ⏱️ **4. Timeout Mechanism**

👉 TCP uses timers to detect packet loss

- If time expires → retransmit
    

---

## 🚦 **5. Flow Control**

👉 Prevents sender from overwhelming receiver

- Uses **sliding window mechanism**
    

---

## 🚧 **6. Error Detection**

👉 Uses checksum to detect errors in data

- Corrupted packets are discarded
    

---

## 🚨 **7. Congestion Control**

👉 Controls traffic in the network

- Avoids overload using algorithms (like slow start)
    

---

## 🔄 **8. Duplicate Detection**

👉 Detects and discards duplicate packets using sequence numbers

---

# ⚡ One-line answer (exam gold)

👉  
**“TCP ensures reliability through sequence numbering, acknowledgments, retransmission, flow control, error detection, and congestion control.”**

---

## 🧠 Quick Memory Trick

👉  
**S A R T F E C D**  
(Sequence, ACK, Retransmit, Timeout, Flow, Error, Congestion, Duplicate)

---

If you want, I can:  
✔ give diagram of TCP flow (very helpful)  
✔ MCQs from this topic  
✔ or compare with UDP in exam style 👍