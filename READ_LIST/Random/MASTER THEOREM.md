
😂 No worries — Master Theorem looks like black magic at first. Let me **de-noodle it** step by step.

We want to solve recurrences of the form:

$$
T(n) = aT\left(\frac{n}{b}\right) + f(n)
$$

*   **$a$** = how many subproblems
*   **$b$** = by how much input size shrinks
*   **$f(n)$** = cost to combine results

The trick: we compare **two growth rates**:

1.  $n^{\log_b a}$ → this is the “work from recursion tree expansion.”
2.  $f(n)$ → this is the “work outside recursion.”

---

### Step 1: Compute $n^{\log_b a}$

*   Take log base $b$ of $a$.
*   Raise $n$ to that power.

👉 Example: if recurrence is $T(n)=2T(n/2)+n$

*   $a=2$, $b=2$
*   $\log_2(2) = 1$ → $n^{1} = n$.

---

### Step 2: Compare $f(n)$ with $n^{\log_b a}$

Now see if $f(n)$ is **smaller, same, or bigger** than that value.

1.  **Case 1 ($f(n)$ smaller)**
    If $f(n)$ grows **polynomially slower** than $n^{\log_b a}$ → recursion dominates.
    Answer: $T(n) = \Theta(n^{\log_b a})$.

2.  **Case 2 ($f(n)$ same size)**
    If $f(n) = \Theta(n^{\log_b a} \cdot \log^k n)$ → balanced case.
    Answer: $T(n) = \Theta(n^{\log_b a} \cdot \log^{k+1} n)$.

3.  **Case 3 ($f(n)$ bigger)**
    If $f(n)$ grows polynomially faster → combining dominates.
    Answer: $T(n) = \Theta(f(n))$.

---

### 🍜 Example Walkthrough (step by step)

**Q:** Solve
$$
T(n) = 2T(n/2) + n
$$

**Step 1:** $a=2, b=2$ → $\log_2(2)=1$ → $n^{1}=n$.
**Step 2:** $f(n) = n$. Compare → $f(n)$ is the same size as $n$.
**Step 3:** Case 2 → $T(n)=\Theta(n \log n)$. ✅

---

**Q:** Solve
$$
T(n) = 7T(n/2) + n^2
$$

**Step 1:** $a=7, b=2$ → $\log_2(7) \approx 2.81$ → $n^{\log_2 7}$.
**Step 2:** $f(n)=n^2$. Compare → $n^2$ is smaller than $n^{\log_2 7}$.
**Step 3:** Case 1 → recursion dominates → $T(n)=\Theta(n^{\log_2 7})$. ✅

---

**Q:** Solve
$$
T(n) = 2T(n/2) + n^2
$$

**Step 1:** $a=2, b=2$ → $\log_2(2)=1$ → $n^1=n$.
**Step 2:** $f(n)=n^2$. Compare → $n^2$ is bigger than $n$.
**Step 3:** Case 3 → combining dominates → $T(n)=\Theta(n^2)$. ✅

---

⚡ So the **only thing you do every time**:

1.  Compute $n^{\log_b a}$.
2.  Compare with $f(n)$.
3.  Pick case 1 / 2 / 3.

---

Do you want me to make you a **visual recipe flowchart** (like: start → compute $\log_b a$ → compare → pick case) so you can follow without memorizing?