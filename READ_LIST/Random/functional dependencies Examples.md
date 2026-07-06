Perfect — yes, this is one of the trickiest but most exam-loved DBMS problems: **finding candidate keys from functional dependencies**.

Let’s practice step by step, starting with **the method**, then solving an example.

---

## 🎯 Method to Find Candidate Keys

Given: Relation `R(A, B, C, D, …)` and a set of FDs.  
We want **candidate keys** (minimal attribute sets that functionally determine all attributes).

**Steps**:

1. **List all attributes** of the relation.
    
2. **Compute closures**: For a set of attributes `X`, compute `X⁺` = all attributes functionally determined by X (using FDs repeatedly).
    
3. **Find superkeys**: If `X⁺` includes _all attributes of R_, then X is a superkey.
    
4. **Check minimality**: If none of X’s proper subsets is also a superkey, then X is a **candidate key**.
    

---

## 📝 Example 1

Relation: `R(A, B, C, D)`  
FDs:

1. A → B
    
2. BC → D
    
3. D → A
    

**Step 1: Compute closures**

- (A)⁺ = {A, B} (from A → B)
    
    - B alone doesn’t give more.
        
    - So (A)⁺ = {A, B}. Not all attributes → not a key.
        
- (B)⁺ = {B}. Not a key.
    
- (C)⁺ = {C}. Not a key.
    
- (D)⁺ = {D, A, B} (D → A, then A → B). Still missing C. Not a key.
    
- (BC)⁺ = {B, C, D, A} (BC → D, then D → A, then A → B).  
    = {A, B, C, D} ✅ → covers all. Superkey!
    

Check minimality:

- B⁺ = {B} (not full).
    
- C⁺ = {C} (not full).  
    So BC is minimal.  
    👉 **Candidate key = {BC}**
    

---

## 📝 Example 2

Relation: `R(P, Q, R)`  
FDs:

1. P → Q
    
2. Q → R
    

- (P)⁺ = {P, Q, R} ✅ → Superkey. Minimal → Candidate key.
    
- (Q)⁺ = {Q, R} (missing P). Not key.
    
- (R)⁺ = {R}. Not key.
    

👉 **Candidate key = {P}**

---

## 📝 Example 3 (trickier)

Relation: `R(W, X, Y, Z)`  
FDs:

1. W → X
    
2. X → Y
    
3. Y → Z
    

- (W)⁺ = {W, X, Y, Z} ✅ → Candidate key.
    
- (X)⁺ = {X, Y, Z} (missing W). Not key.
    
- (Y)⁺ = {Y, Z}. Not key.
    
- (Z)⁺ = {Z}. Not key.
    

👉 **Candidate key = {W}**

---

⚡ Practice Strategy:

- Always start with single attributes.
    
- Then pairs, then triples, etc.
    
- Watch out: Sometimes there are **multiple candidate keys**.
    

---

## second one
Great — let’s solve this **step-by-step** and keep it crisp.

Relation: `R(A,B,C,D,E)`  
FDs:

1. `A → BC`
    
2. `CD → E`
    
3. `B → D`
    

### Step 1 — try single-attribute closures

- **A⁺**: start `{A}`
    
    - `A → BC` → add `B, C` ⇒ `{A,B,C}`
        
    - `B → D` → add `D` ⇒ `{A,B,C,D}`
        
    - `CD → E` (now have `C` and `D`) → add `E` ⇒ `{A,B,C,D,E}`  
        ⇒ **A⁺ = {A,B,C,D,E}** → covers all attributes → **A is a superkey**. Since it’s a single attribute, it’s minimal → **A is a candidate key**.
        
- **B⁺**: start `{B}`
    
    - `B → D` → `{B,D}`. No `C`, so `CD → E` not usable; no rule gives `A`.  
        ⇒ **B⁺ = {B,D}** (not all attributes)
        
- **C⁺** = `{C}` (no FDs fire)
    
- **D⁺** = `{D}`
    
- **E⁺** = `{E}`
    

None of B, C, D, E are keys alone.

### Step 2 — do we need to check combos?

We already found `A` is a candidate key. Ask: **could there be other candidate keys that do not contain A?**  
To be a key they must determine `A`. But no FD has `A` on the right-hand side, so **no combination of attributes that excludes A can ever determine A** (because nothing gives A). Therefore **every candidate key must include A**. Since `{A}` itself is a key and is minimal, there are **no other candidate keys**.

### Final answer

**Candidate key(s): `{A}`**

---

Want another problem (I’ll make it slightly harder — multiple candidate keys possible) so you can practice finding multiple keys?