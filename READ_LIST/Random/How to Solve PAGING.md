Ohhh yes — this is a **classic memory management (Paging) question type**. Let’s build a mini question bank with **step-by-step answers** so you can practice.

---

## 🔹 Paging
	the storing mechanism to retreive data from secondary storage to main memory in the form of a page...

Given:
- **Logical Address (LA)** = X
- **Page Size (PS)** = P (power of 2, like 512, 1024, 2048, …)

👉 **Page Number** = `LA ÷ PS` (integer division).  
👉 **Offset** = `LA mod PS` (remainder).

---
## 🔹 Practice Questions


![[Pasted image 20251015204728.png|Paging..]]

### **Q1.**

Logical Address = `4000`, Page Size = `1 KB (1024)`

- Page number = `4000 ÷ 1024 = 3` (since 1024×3 = 3072, remainder left)
    
- Offset = `4000 % 1024 = 4000 – 3072 = 928`  
    ✅ **Answer: Page = 3, Offset = 928**
    

---

### **Q2.**

Logical Address = `2050`, Page Size = `512`

- Page number = `2050 ÷ 512 = 4`
    
- Offset = `2050 mod 512 = 2`  
    ✅ **Answer: Page = 4, Offset = 2**
    

---

### **Q3.**

Logical Address = `6000`, Page Size = `2 KB (2048)`

- Page number = `6000 ÷ 2048 = 2`
    
- Offset = `6000 mod 2048 = 1904`  
    ✅ **Answer: Page = 2, Offset = 1904**
    

---

### **Q4.**

Logical Address = `1023`, Page Size = `512`

- Page number = `1023 ÷ 512 = 1`
    
- Offset = `1023 mod 512 = 511`  
    ✅ **Answer: Page = 1, Offset = 511**
    

---

### **Q5. (Tricky one)**

Logical Address = `8192`, Page Size = `1 KB (1024)`

- Page number = `8192 ÷ 1024 = 8`
    
- Offset = `8192 mod 1024 = 0`  
    ✅ **Answer: Page = 8, Offset = 0** (exact multiple)
    

---

## 🔹 MCQ Tip

If the page size = `2ᵏ`, then:

- **Page number = higher (address bits – k bits)**
    
- **Offset = lower k bits**
    

E.g., Page size = 1 KB → offset = 10 bits, rest are page number.

---
### **Q1. Offset Calculation**

Logical address = `0x1234AB` (hex), Page size = `4KB`.

- Page size = 2¹² → offset = **==12 bits = 3 hex digits==**.
- Page size = 4 KB = $2^{12}$ bytes → **offset = lower 12 bits** = **3 hex digits**.
    
- Offset = `0x4AB`.
- Hex = `0x123`
    
- Page number = remaining bits = `0x123`.  
    ✅ **Answer: Page = 0x123, Offset = 0x4AB**

---
### **Q3. Address Breakdown**

Logical address = 32-bit, Page size = 4KB.

- Offset bits = log₂(4096) = 12.
    
- Page number bits = 32 – 12 = 20 bits.  
    ✅ **Answer: Page number = 20 bits, Offset = 12 bits**
    

---

### **Q4. Trick (Exact Multiple of Page Size)**

Logical address = 8192, Page size = 4KB (4096).

- Page number = 8192 ÷ 4096 = 2.
    
- Offset = 8192 mod 4096 = 0.  
    ✅ **Answer: Page = 2, Offset = 0**