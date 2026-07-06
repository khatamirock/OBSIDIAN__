
# 🔹 1. Big-O (Upper Bound)

**Definition:**  
We say `f(n) ∈ O(g(n))` if there exist constants `c > 0` and `n₀ ≥ 0` such that

`0 ≤ f(n) ≤ c · g(n)` for all `n ≥ n₀`.

👉 Meaning: f(n) does not grow faster than g(n), up to a constant multiple.  
It gives a **worst-case upper bound**.

**Example:** `f(n) = 3n + 5`, `g(n) = n`.  
Take `c = 4`, `n₀ = 5`. For all n ≥ 5, `3n+5 ≤ 4n`.  
So `f(n) ∈ O(n)`.

---

# 🔹 2. Big-Ω (Lower Bound)

**Definition:**  
We say `f(n) ∈ Ω(g(n))` if there exist constants `c > 0` and `n₀ ≥ 0` such that

`0 ≤ c · g(n) ≤ f(n)` for all `n ≥ n₀`.

👉 Meaning: f(n) does not grow slower than g(n).  
It gives a **best-case lower bound**.

**Example:** `f(n) = 3n + 5`, `g(n) = n`.  
Take `c = 2`, `n₀ = 5`. For all n ≥ 5, `2n ≤ 3n+5`.  
So `f(n) ∈ Ω(n)`.

---

# 🔹 3. Big-Θ (Tight Bound)

**Definition:**  
We say `f(n) ∈ Θ(g(n))` if there exist constants `c₁ > 0`, `c₂ > 0`, and `n₀ ≥ 0` such that

`0 ≤ c₁·g(n) ≤ f(n) ≤ c₂·g(n)` for all `n ≥ n₀`.

👉 Meaning: f(n) grows at the **same rate** as g(n), up to constant factors.  
It’s a **tight bound** (both upper and lower).

**Example:** `f(n) = 3n + 5`, `g(n) = n`.  
Take `c₁ = 2`, `c₂ = 4`, `n₀ = 5`. Then `2n ≤ 3n+5 ≤ 4n`.  
So `f(n) ∈ Θ(n)`.

---

# 🔹 4. Little-o (Strict Upper Bound)

**Definition:**  
We say `f(n) ∈ o(g(n))` if for every constant `c > 0`, there exists `n₀ ≥ 0` such that

`0 ≤ f(n)` ==<== `c · g(n)` for all `n ≥ n₀`.

👉 Meaning: f(n) grows **==strictly== slower** than g(n).  
As n → ∞, `f(n)/g(n) → 0`.

**Example:** `f(n) = n`, `g(n) = n²`.  
Then `n/n² = 1/n → 0`.  
So `n ∈ o(n²)`.

---

# 🔹 5. Little-ω (Strict Lower Bound)

**Definition:**  
We say `f(n) ∈ ω(g(n))` if for every constant `c > 0`, there exists `n₀ ≥ 0` such that

`0 ≤ c · g(n) < f(n)` for all `n ≥ n₀`.

👉 Meaning: f(n) grows **strictly faster** than g(n).  
As n → ∞, `f(n)/g(n) → ∞`.

**Example:** `f(n) = n²`, `g(n) = n`.  
Then `n²/n = n → ∞`.  
So `n² ∈ ω(n)`.

---

# 🎯 Summary Table

|Notation|Bound Type|Formal condition|Intuition|
|---|---|---|---|
|**O(g(n))**|Upper bound|`f(n) ≤ c·g(n)`|f grows at most like g|
|**Ω(g(n))**|Lower bound|`f(n) ≥ c·g(n)`|f grows at least like g|
|**Θ(g(n))**|Tight bound|`c₁·g(n) ≤ f(n) ≤ c₂·g(n)`|f grows exactly like g|
|**o(g(n))**|Strict upper|`f(n)/g(n) → 0`|f grows strictly slower than g|
|**ω(g(n))**|Strict lower|`f(n)/g(n) → ∞`|f grows strictly faster than g|

---

Would you like me to also show you **how to actually pick constants c and n₀** in a sample exam question (like proving `3n+7 ∈ O(n)` step by step)?