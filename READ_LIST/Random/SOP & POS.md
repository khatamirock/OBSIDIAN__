## 10) Quick reference (what to tick in MCQs)

- If question: “SOP corresponds to minterms” → **True**.
    
- “POS corresponds to maxterms” → **True**.
    
- “Canonical SOP terms may omit variables” → **False** (canonical must include all vars).
    
- “SOP is implemented by OR-AND network” → **False** (SOP is AND-OR; POS is OR-AND).
    
- “If function has few 1s, canonical SOP is compact” → **True**.
    
- “Minterm index for A=1,B=0,C=1 is 5” → **True** (binary 101 → 5).
    

---

## 11) 8 Practice MCQs (with short answers)

1. **Q:** `F(A,B) = 1` only for (A,B) = (0,1). Canonical SOP is:  
    A) `A'B` B) `A' + B` C) `(A + B')` D) `A + B'`  
    **Ans:** A (`A'B`) — minterm for 01.
    
2. **Q:** Which form is `F = (A + B')(A' + C)`?  
    A) SOP B) POS C) canonical SOP D) canonical POS  
    **Ans:** B (POS). Not canonical (terms missing variables).
    
3. **Q:** `F = Σ m(1,2)` for 3 variables. Which is correct simplification?  
    A) `A'B'C' + A'BC'` B) `A' C'` C) `B' C'` D) `A'B'`  
    **Ans:** B (`A' C'`) — factor: A' C' (B' + B).
    
4. **Q:** Minterm index for `A=1,B=1,C=0` is:  
    A) 6 B) 3 C) 5 D) 7  
    **Ans:** A (110₂ = 6).
    
5. **Q:** A canonical POS expression must:  
    A) Have sums with all variables. B) Use only complemented variables. C) Have products with few variables. D) Be simplified.  
    **Ans:** A.
    
6. **Q:** If `F = Σ m(0,3,7)` (3 vars), how many minterms does F have?  
    A) 1 B) 2 C) 3 D) 4  
    **Ans:** C (three minterms listed).
    
7. **Q:** Which is true? `F = Σ m(0,2)` ⇒ `F' = Σ m(1,3,4,5,6,7)`?  
    A) True B) False  
    **Ans:** A (complement covers other indices).
    
8. **Q:** In K-map simplification, grouping a 2×2 square eliminates how many variables?  
    A) 1 B) 2 C) 3 D) 0  
    **Ans:** B (2 variables drop; group of 4 -> drops 2 variables; group size 2^k --> drops k variables).
    

---

## 12) Final short checklist for exams

- If asked “SOP or POS?” → check whether they list indices of 1s (SOP) or 0s (POS).
    
- If they say “canonical” → every term must contain **all** variables.
    
- To convert truth table → SOP: list 1-rows → write minterms. To convert → POS: list 0-rows → write maxterms.
    
- For simplification use K-map: group powers of two; always check essential prime implicants.