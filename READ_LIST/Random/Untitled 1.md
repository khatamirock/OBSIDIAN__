

## Sum Of Products (SOP) and Products of Sum (POS):
Here's the OCR of the image:

**Example**

| a   | b   | c   | f₁  |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 1   |
| 0   | 1   | 1   | 0   |
| 1   | 0   | 0   | 1   |
| 1   | 0   | 1   | 0   |
| 1   | 1   | 0   | 1   |
| 1   | 1   | 1   | 0   |

- Truth table for f₁(a,b,c) at right
- The canonical sum-of-products form for f₁ is  
    f₁(a,b,c) = m₁ + m₂ + m₄ + m₆  
    = a'b'c + a'bc' + ab'c' + abc'

- The canonical product-of-sums form for f₁ is  
    f₁(a,b,c) = M₀ • M₃ • M₅ • M₇  
    = (a+b+c)•(a+b'+c')•(a'+b+c')•(a'+b'+c').

- Observe that: mⱼ = Mⱼ'
---

**Canonical** means: _"using all variables in every term"

## Conversion of SOP from Standard to Canonical Form

**Step 1:** Expand non-canonical terms by inserting the equivalent of 1 in each missing variable  
(using the identity: $x+x′=1$)

**Step 2:** Remove duplicate minterms

---

Given:

$f1(a,b,c)=a′b′c+bc′+ac$
$′f_1(a,b,c) = a'b'c + bc' + ac'$

**Expansion:**

=$a′b′c+(a+a′)bc′+a(b+b′)c′$
= $a'b'c + abc' + a'bc' + abc' + ab'c'$

**After removing duplicates:**

= $a'b'c + abc' + a'bc' + ab'c'$


---
Here's the OCR of the image:

- Expand noncanonical terms by adding 0 in terms of missing variables (e.g., xx' = 0) and using the distributive law
    
- Remove duplicate maxterms

Given:
- f₁(a,b,c) = (a+b+c)•(b'+c')•(a'+c')  
Expansion:
    = (a+b+c)•(aa'+b'+c')•(a'+bb'+c')  
    = (a+b+c)•(a+b'+c')•(a'+b+c')•(a'+b'+c')•(a'+b+c')•(a'+b'+c')  

After removing duplicates:
    = (a+b+c)•(a+b'+c')•(a'+b+c')•(a'+b'+c')