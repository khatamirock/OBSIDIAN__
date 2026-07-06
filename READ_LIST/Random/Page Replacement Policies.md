[[OS#**Page Replacement Algorithms **|more....]]
## 1. **FIFO (First-In First-Out)**

- Oldest page in memory is replaced first.
- **Easy, but dumb.**
- Can suffer from **Belady’s Anomaly** → more frames can cause **more** page faults.
- MCQ Trap: If asked _which policy suffers from Belady’s anomaly?_ → **FIFO**.

---

## 2. **Optimal (OPT / MIN)**

- Replace the page that will **not be used for the longest time in the future**.
    
- **Best possible** (==minimum faults==), but **==not implementable==** in practice (because ==future is unknown==).
    
- Used ⭐⚠️==as a **benchmark**==.
    
- MCQ Trap: “Which algorithm gives minimum number of page faults?” → **Optimal**.
    

---

## 3. **LRU (Least Recently Used)**

- Replace the page that was **least recently used in the past**.
    
- Works well if **past ≈ future** (locality of reference).
    
- Requires hardware ⭐⚠️(counters/timestamps/stack).
    
- **Most practical** among real ones.
    
- MCQ Trap: “Which replacement approximates Optimal?” → **LRU**.
    

---

## 4. **LFU (Least Frequently Used)**

- Replace the page used **least number of times**.
    
- Problem: **Old pages that were once used heavily may stay forever** (not fair).
    
- Teachers ask: “Which replacement suffers from _cache pollution_ due to old frequently-used pages?” → **LFU**.
    

---

## 6. **Second-Chance (Clock Algorithm)**

- Improvement of FIFO.
    
- Each page has a **reference bit**:
    
    - If 0 → replace.
        
    - If 1 → give a “second chance” and clear the bit, move on.
        
- Implemented like a circular queue (clock hand).
    
- Practical **approximation to LRU**.
    
- MCQ Trap: “Which policy is FIFO with modification using reference bit?” → **Second Chance (Clock)**.
    

---

# 🔥 Quick Comparison (must know for MCQ)

| Policy            | Notes / Traps                                             |
| ----------------- | --------------------------------------------------------- |
| **FIFO**          | Simple, suffers from **==Belady’s anomaly==**             |
| **Optimal**       | Best (benchmark), **impossible in practice**              |
| **LRU**           | Practical, approximates Optimal, **no Belady’s anomaly**  |
| **LFU**           | Keeps old frequently-used pages forever (cache pollution) |


---

# 📝 Classic Exam Questions

1. Which algorithm can never suffer from Belady’s anomaly? → **Optimal, LRU**
    
2. Which algorithm may give more faults with more frames? → **FIFO**
    
3. Which is impossible to implement? → **Optimal**
    
4. Which uses reference bit? → **Clock (Second Chance)**
    
5. Which has lowest overhead? → **Random**
    
6. Which is most practical real-world? → **LRU / Clock**
    
7. LFU vs MFU trick:
    
    - LFU = replaces least used page.
        
    - MFU = replaces most used page (on assumption “if used a lot, won’t be used again”).
        

---

✅ **Shortcut**:

- **Best theoretical** = Optimal
    
- **Best practical** = LRU (or Clock)
    
- **Trick anomaly** = FIFO
    
- **Frequency-based trap** = LFU vs MFU
    

---

Do you want me to **make practice MCQs (with small reference strings and frame sizes)** so you can try calculating page faults under FIFO, LRU, Optimal (the ones teachers love to torture with)?