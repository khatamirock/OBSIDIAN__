
### 1. What is a linear homogeneous recurrence?

A recurrence relation defines each term of a sequence using earlier terms.
A linear homogeneous recurrence of order 2 looks like:

$$a_n = c_1 a_{n-1} + c_2 a_{n-2}$$

-   *Linear* = only linear combinations of earlier terms.
-   *Homogeneous* = there is no extra function of $n$ added (no “+ f(n)” term).

You solve it to get a formula for $a_n$ (closed form) rather than computing term by term.

### 2. The standard method (Characteristic equation) — very mechanical

**Step A — form the characteristic equation**

Replace $a_n$ by $r^n$. You get:

$$r^n = c_1 r^{n-1} + c_2 r^{n-2}$$

Divide by $r^{n-2}$ (assuming $r \neq 0$) → the characteristic polynomial:

$$r^2 - c_1 r - c_2 = 0$$

Solve that quadratic for roots $r_1, r_2$.

**Step B — use one of two cases**

*   **Case 1 — distinct roots $r_1 \neq r_2$:**
    General solution:
    $$a_n = \alpha (r_1)^n + \beta (r_2)^n$$

*   **Case 2 — repeated root $r_1 = r_2 = r$:**
    General solution:
    $$a_n = \alpha (r)^n + \beta n (r)^n$$

**Step C — determine $\alpha, \beta$**

Use given initial conditions (typically $a_0$ and $a_1$) to form two linear equations and solve for $\alpha, \beta$.

### 3. Worked example — distinct roots (nice integers)

Recurrence:
$$a_n = 5a_{n-1} - 6a_{n-2}, \quad a_0=1, \ a_1=5$$

Characteristic equation:
$$r^2 - 5r + 6 = 0$$
Factor: $(r-2)(r-3) = 0$. So $r_1=2, r_2=3$.

General form:
$$a_n = \alpha 2^n + \beta 3^n$$

Use initial conditions:
-   For $n=0$: $a_0 = \alpha + \beta = 1$.
-   For $n=1$: $a_1 = 2\alpha + 3\beta = 5$.

Solve:
From the first equation: $\alpha = 1 - \beta$.
Plug into the second: $2(1-\beta) + 3\beta = 5 \implies 2 - 2\beta + 3\beta = 5 \implies \beta = 3$.
Then $\alpha = 1 - 3 = -2$.

Final closed form:
$$a_n = -2 \cdot 2^n + 3 \cdot 3^n$$

*Quick check for $n=2$*:
-   Using the formula: $a_2 = -2 \cdot 2^2 + 3 \cdot 3^2 = -8 + 27 = 19$.
-   Using the recurrence: $a_2 = 5a_1 - 6a_0 = 5(5) - 6(1) = 25 - 6 = 19$. It works.

### 4. Worked example — repeated root

Recurrence:
$$a_n = 2a_{n-1} - a_{n-2}, \quad a_0=1, \ a_1=2$$

Characteristic equation:
$$r^2 - 2r + 1 = 0 \implies (r-1)^2 = 0$$
This gives a repeated root $r=1$.

General form for a repeated root:
$$a_n = \alpha \cdot 1^n + \beta n \cdot 1^n = \alpha + \beta n$$

Use initial conditions:
-   $a_0 = \alpha + \beta \cdot 0 = \alpha = 1$.
-   $a_1 = \alpha + \beta = 2 \implies 1 + \beta = 2 \implies \beta = 1$.

So the closed form is:
$$a_n = 1 + n$$

*Quick check*:
If $a_n = n+1$, then the RHS of the recurrence is $2a_{n-1} - a_{n-2} = 2(1+(n-1)) - (1+(n-2)) = 2n - (n-1) = n+1$. This matches the LHS, $a_n$. It works.

### 5. Short recipe you can memorize

1.  Form the characteristic polynomial $r^2 - c_1 r - c_2 = 0$.
2.  Solve for the roots $r_1, r_2$.
3.  If $r_1 \neq r_2$: $a_n = \alpha r_1^n + \beta r_2^n$.
4.  If there is a repeated root $r$: $a_n = \alpha r^n + \beta n r^n$.
5.  Plug in $n=0, 1$ (or whichever initial conditions you have) to find $\alpha, \beta$.

### 6. Generating functions — what they are and two easy examples

A generating function encodes a sequence $(a_0, a_1, a_2, \dots)$ as a power series:
$$G(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \dots$$
It is a tool to manipulate sequences algebraically.

**Example A — constant sequence $1, 1, 1, \dots$**

Let $a_n = 1$ for all $n$. Then
$$G(x) = 1 + x + x^2 + x^3 + \dots = \frac{1}{1-x} \quad (\text{for } |x|<1)$$

**Example B — geometric sequence $1, a, a^2, a^3, \dots$**

Let $a_n = a^n$. Then
$$G(x) = 1 + ax + a^2x^2 + a^3x^3 + \dots = \frac{1}{1-ax}$$

These are basic algebraic identities you can derive by multiplying by $x$ and subtracting.