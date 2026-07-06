### Example 1: Basic Page

![[EMAT2_os.png]]




---
**==Q==**: A paging scheme using TLB. TLB access time 10ns and main memory access time taken 50 ns. What is the effective memory access time if TLB hit ratio is 90% and there is no page fault.**

To compute the **effective memory access time (EMAT)** with a **TLB**, you consider two scenarios: a **TLB hit** and a **TLB miss**. These are weighted by their respective probabilities, the **hit ratio** (h) and **miss ratio** (1−h).

---
## TLB Hit (Probability h)

- **Time to check TLB** (TTLB​): 10ns
- **Time to read from memory** (once) (Tmem​): 50ns

The total time on a TLB hit (Thit​) is:

Thit​=$T_{TLB​}+T_{mem}$ ​=10+50=60ns

---

## TLB Miss (Probability 1−h)

- **Time to check TLB** (fail) (TTLB​): 10ns
- **Time to read page table entry from memory** (Tmem​): 50ns
- **Time to then read the actual data from memory** (another Tmem​): 50ns

The total time on a TLB miss (Tmiss​) is:

$T_{miss}​=T_{TLB}​+2⋅T_{mem}$​=10+2⋅50=110ns

---

## Combining with Hit Ratio (h=0.9)

Now, we combine the times for a hit and a miss using the given hit ratio h=0.9:

EMAT=$h×T_{hit} ​+ (1−h)×T_{miss​}$

EMAT= $0.9×60  +  0.1×110$

EMAT= $54+11$

EMAT=$65$ ns



---
### 🧮 Example: ==Cache== Memory — Effective Access Time (EMAT) 
-  ==2nd type math== 

**Given:**

- Cache hit ratio: $$h = 0.85$$
- Cache access time: $$t_c = 10 \text{ ns}$$
    
- Main memory access time: $$t_m = 80 \text{ ns}$$
**Formula:**

$$  
\text{EMAT} = h \cdot t_c + (1 - h) \cdot (t_c + t_m)  
$$

---

**Substitute values:**

$$  
\text{EMAT} = 0.85 \cdot 10 + (1 - 0.85) \cdot (10 + 80)  
$$
$$  
\text{EMAT} = 8.5 + 0.15 \cdot 90  
$$
$$  
\text{EMAT} = 8.5 + 13.5 = 22 \text{ ns}  
$$

---

**✅ Final Answer:**
$$  
\boxed{\text{EMAT} = 22 \text{ ns}}  
$$

---

## ✅ Problem 1: Calculating Effective Memory Access Time (EMAT)

**Given:**

- Main memory access time = 20ns
- Page fault service time = 100ns
- Page fault rate = 65%

**Question:**

Calculate the effective memory access time (EMAT).

---

### Solution:

The formula for EMAT in this context is:
> Simple case

$EMAT=(1−p)×Memory\ Access\ Time+p × Page\ Fault\ Service\ Time$
> p = Page fault Ratio



Where:

- p = page fault rate

Plugging in the given values:

p=0.65 (since the page fault rate is 65%)

Memory Access Time = 20ns

$Page\ Fault\ Service\ Time = 100ns$
EMAT=$(1−0.65)×20ns+0.65×100\ ns$

EMAT=0.35×20+0.65×100

EMAT=7+65

EMAT=72ns​


---

**==Q :**== **Consider a paging system with page table stored in memory.**

**a. If memory reference take 100 ns, how long does a pagged memory reference take?**

**b. If we add a TLB with 90% hit ratio, What will be the EMAT?**
**(Assume TLB access time = 15 ns)**

---
Here's the solution formatted for Obsidian:

---

## Solution: Paging System Memory Access

### a. "Paged" Memory Reference (No TLB)

When the page table resides in main memory, each logical memory reference requires two memory accesses:

1. **One memory access** to read the page-table entry to find the physical address.
2. **One memory access** to fetch the actual data using the physical address.

Given:

Memory access time ($T_{mem}$​) = 100ns

Total time per paged memory reference ($T_{paged}$​):

$T_{paged}$​​ = 2×$T_{mem​}$
$T_{paged}$​​ = 2×100ns
$T_{paged}$​ ​= 200ns​

---

### b. With a TLB (90% hit ratio, TLB access = 15 ns)

Let's define the given values:

- TLB hit ratio (h) = 0.90
- TLB access time (TTLB​) = 15ns
- Memory access time (Tmem​) = 100ns

#### 1. On a TLB Hit (Probability h)

If the entry is found in the TLB:

- Check TLB: TTLB​
- Fetch data from memory: Tmem​

Total time on a TLB hit (Thit​):

Thit ​=$t​+m$

Thit​=15+100

Thit​=115ns

#### 2. On a TLB Miss (Probability 1−h)

If the entry is not found in the TLB:

- Check TLB (fails): TTLB​
- Read page-table entry from memory: Tmem​ (This is to get the physical address from the page table)
- Then read data from memory: Tmem​ (This is to fetch the actual data)

Total time on a TLB miss (Tmiss​):

Tmiss​ = $t​+2×m$

Tmiss ​= 15+2×100

Tmiss​ =15+200

Tmiss​ =215ns

#### 3. Combine for EMAT

The Effective Memory Access Time (EMAT) is calculated by weighting the hit and miss times by their probabilities:

EMAT=h×Thit​+(1−h)×Tmiss​

EMAT=0.90×115+(1−0.90)×215

EMAT=0.90×115+0.10×215

EMAT=103.5+21.5

EMAT=125ns​

---

### Summary:

- **(a) Paged Memory Reference (no TLB):** 200ns per reference.
- **(b) With a 90% TLB hit rate and 15 ns TLB lookup:** EMAT=125ns.


---

# Paging: Address Mapping Example

### 1️⃣ Address Spaces

- **Logical Address Space (LAS)** = Address space seen by the CPU/program.
- **Physical Address Space (PAS)** = Actual RAM locations.
- Both are divided into **pages** (LAS) and **frames** (PAS).
- **Page Size = Frame Size** (must be same).

---

### 2️⃣ Example

- **Physical Address = 12 bits** → PAS = 2¹² = 4K words.
- **Logical Address = 13 bits** → LAS = 2¹³ = 8K words.
- Assume **Page size = Frame size = 1K words**.


👉 **Number of Frames** = PAS / Frame Size = 4K / 1K = 4 = 2==²==  
👉 **Number of Pages** = LAS / Page Size = 8K / 1K = 8 = 2==³==

---

### 3️⃣ Breaking the Address

- **Logical Address** (13 bits) → `p + d`
    
    - `p` = page number (needs ==3 bits== to represent 8 pages).
    - `d` = page offset (needs 10 bits to represent 1K words).
- **Physical Address** (12 bits) → `f + d`
    
    - `f` = frame number (needs ==2 bits== to represent 4 frames).
    - `d` = frame offset (10 bits, same as page offset).