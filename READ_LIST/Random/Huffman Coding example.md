

A:5, B:9, C:12, D:13, E:16, F:45

### Correct merges (always pick the **two smallest** remaining)

1. Merge A(5) + B(9) → node AB = 14.  
    Remaining: 12(C), 13(D), 14(AB), 16(E), 45(F)
    
2. Merge C(12) + D(13) → node CD = 25.  
    Remaining: 14(AB), 16(E), 25(CD), 45(F)
    
3. Merge AB(14) + E(16) → node ABE = 30.  
    Remaining: 25(CD), 30(ABE), 45(F)
    
4. Merge CD(25) + ABE(30) → node W = 55.  
    Remaining: 45(F), 55(W)
    
5. Merge F(45) + W(55) → root = 100.
    

(You were absolutely right that after creating 14, the next two smallest were 12 and 13 — that’s what I should have done. My earlier step incorrectly paired 14 with 12. Sorry.)

---

### One valid set of Huffman codes (choose smaller child = left = `0` for each merge)

Following the tree built above (small child → left → `0`):

- F = `0`
    
- C = `100`
    
- D = `101`
    
- A = `1100`
    
- B = `1101`
    
- E = `111`
    

(There are multiple valid Huffman code sets depending on minor tie-breaking choices, but this one matches the merges listed.)

---

### Check — total bits (weighted sum)

Compute `frequency × code length`:

- F: 45 × 1 = 45
    
- C: 12 × 3 = 36
    
- D: 13 × 3 = 39
    
- E: 16 × 3 = 48
    
- A: 5 × 4 = 20
    
- B: 9 × 4 = 36
    

**Total = 45 + 36 + 39 + 48 + 20 + 36 = 224 bits.**

---

### Example encoding (same example as before)

Encode `"FACE"`:

- F → `0`
    
- A → `1100`
    
- C → `100`
    
- E → `111`  
    Concatenation: `0 1100 100 111` → `01100100111` (11 bits)
    

---

If you want, I can:

- draw the tree (ASCII) so you can see where each code comes from, or
    
- give another worked example with different frequencies so you can practise the merge steps.
    

Again — nice catch. Thanks for calling that out. Want the tree picture next?

---

## 🔹 Example 2: Small case

Characters:

- X = 7
    
- Y = 5
    
- Z = 2
    

Steps:

- Take Z(2), Y(5) → combine = 7.
    
- Now X(7), 7 → combine = 14.
    

Assign codes:

- X = 0
    
- Y = 10
    
- Z = 11
    

So string `"XYZ"` encodes as `0 10 11 = 01011` (5 bits).  
Fixed code would need 2 bits each → 6 bits.

---

## 🎯 What exam may ask

1. **“What is the Huffman code for a given character?”**  
    → You must show path in tree.
    
2. **“How many bits to encode a given string?”**  
    → Multiply length of code × frequency.
    
3. **Trap:** If you mis-combine smallest frequencies in the wrong order, the whole coding changes.
    

---

👉 Do you want me to prepare a **step-by-step worked MCQ style example** (like what you’ll see in exam), where they give frequencies and ask for total number of bits?