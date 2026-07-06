---
GREY CODUS:
cssclasses:
asdasd:
---

**Rule:**  
Keep the **most significant bit (MSB)** same.  
Each next Gray bit = XOR of current binary bit and the previous binary bit.

**Formula:**  
G₁ = B₁  
Gᵢ = Bᵢ ⊕ Bᵢ₋₁

**Example:**  
Binary = `1011`  
→ G₁ = ==1==  
→ G₂ = ==0==⊕1 = 1  
→ G₃ = ==1==⊕0 = 1  
→ G₄ = ==1==⊕1 = 0  
✅ **==Gray== Code = 1110**

---

### 🔁 **2. Gray Code → Binary**

**Rule:**  
Keep MSB same.  
Each next Binary bit = XOR of previous Binary bit and current Gray bit.

**Formula:**  
B₁ = G₁  
Bᵢ = Bᵢ₋₁ ⊕ Gᵢ

**Example:**  
Gray = `1110`  
→ B₁ = ==1==  
→ B₂ = 1⊕==1== = 0  
→ B₃ = 0⊕==1== = 1  
→ B₄ = 1⊕==0== = 1  
✅ **==Binary== = 1011**

---

**In short:**

|Conversion|Formula|Keep MSB|Operation for rest|
|---|---|---|---|
|Binary → Gray|Gᵢ = Bᵢ ⊕ Bᵢ₋₁|Same as Binary|XOR adjacent bits|
|Gray → Binary|Bᵢ = Bᵢ₋₁ ⊕ Gᵢ|Same as Gray|XOR with previous Binary|

---

Sure bro 👇 let’s take another example for **Gray → Binary conversion** step-by-step.

---

### Example 1

Gray code: `1010`

**Step 1:**  
B₁ = G₁ = 1

**Step 2:**  
B₂ = B₁ ⊕ G₂ = 1 ⊕ 0 = 1

**Step 3:**  
B₃ = B₂ ⊕ G₃ = 1 ⊕ 1 = 0

**Step 4:**  
B₄ = B₃ ⊕ G₄ = 0 ⊕ 0 = 0

✅ **Binary = 1100**

---

### Example 2

Gray code: `0111`

**Step 1:**  
B₁ = G₁ = 0

**Step 2:**  
B₂ = B₁ ⊕ G₂ = 0 ⊕ 1 = 1

**Step 3:**  
B₃ = B₂ ⊕ G₃ = 1 ⊕ 1 = 0

**Step 4:**  
B₄ = B₃ ⊕ G₄ = 0 ⊕ 1 = 1

✅ **Binary = 0101**

---

### Quick recap:

To convert **Gray → Binary**  
→ copy first bit  
→ keep XORing with the next Gray bit.

So:  
**1010 → 1100**  
**0111 → 0101**