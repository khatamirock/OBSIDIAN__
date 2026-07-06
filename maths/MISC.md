1. To find the last digit of $4^{11}$, I'll track the pattern of last digits in powers of 4.
	Let me calculate the last digits of successive powers of 4:
	
	- 4^1 = 4 → last digit is 4
	- 4^2 = 16 → last digit is 6
	- 4^3 = 64 → last digit is 4
	- 4^4 = 256 → last digit is 6
	- 4^5 = 1024 → last digit is 4
	- 4^6 = 4096 → last digit is 6
	
	I can see the pattern now: the last digit of powers of 4 alternates between 4 and 6.
	
	Since this pattern has a cycle of 2, I need to determine whether 11 is odd or even:
	
	- 11 is odd
	- Odd powers of 4 end with the digit 4
	- - Odd exponents (1, 3, 5, ...): Last digit is **4**.
	- Even exponents (2, 4, 6, ...): Last digit is **6**.
	
	Therefore, the last digit of $4^{11}$, is 4.

2.  formulas to calculate 1+2+3.......n  &  1^2+2^2+3^2+,................... and also the power of 3
	Here are the key formulas for those series:
	For the sum of first n natural numbers (1+2+3+...+n):
	```
	Sum = n(n+1)/2
	```
	For the sum of squares of first n natural numbers (1²+2²+3²+...+n²):
	
	```
	Sum = n(n+1)(2n+1)/6
	```
	
	For the sum of cubes of first n natural numbers (1³+2³+3³+...+n³):
	```
	Sum = [n(n+1)/2]²
	```
	
	These formulas are quite useful for solving problems without having to calculate each term individually.



3. Since you’re preparing for exams and want a comprehensive yet concise resource for basic geometric and algebraic formulas, I’ll provide a structured breakdown of calculations for triangles (different types), circles, and other common shapes, followed by key algebraic identities and equations (e.g., quadratic, cubic). This will be formatted in a way that’s perfect for your Obsidian notes—clear, memorable, and exam-ready. I’ll focus on the essentials, avoiding overly complex derivations, and include examples where helpful.

---

## Basic Geometric and Algebraic Formulas

### Geometric Formulas

#### 1. Triangles (ত্রিভুজ)
Triangles come in different types (scalene, isosceles, equilateral, right-angled), and their calculations vary based on given data.

| **Type**                           | **Area Formula**                                    | **Perimeter**   | **Notes**                                                                          |
| ---------------------------------- | --------------------------------------------------- | --------------- | ---------------------------------------------------------------------------------- |
| **General Triangle**               | \( $\text{Area} = \frac{1}{2} \times b \times h$ \) | \( a + b + c \) | \( b \) = base, \( h \) = height (perpendicular to base).                          |
| **Equilateral (সমবাহু)**           | \( $\text{Area} = \frac{\sqrt{3}}{4} \times s^2$ \) | \( 3s \)        | \( s \) = side length; all sides and angles (60°) equal.                           |
| **Right-Angled (সমকোণী)**          | \( $\text{Area} = \frac{1}{2} \times a \times b$ \) | \( a + b + c \) | \( a, b \) = legs, \( c = \sqrt{a^2 + b^2} \) (Pythagoras: \( a^2 + b^2 = c^2 \)). |
| **Heron’s Formula (any triangle)** | $( \text{Area} = \sqrt{s(s-a)(s-b)(s-c)}$ )         | \( a + b + c \) | \( s = \frac{a + b + c}{2} \) (semi-perimeter), \( a, b, c \) = sides.             |

- **Example**: Right triangle with legs 3 and 4:
  - Hypotenuse = \( $\sqrt{3^2 + 4^2} = 5$ \)
  - Area = \( $\frac{1}{2} \times 3 \times 4 = 6$ \)
  - Perimeter = \( 3 + 4 + 5 = 12 \)

#### 2. Circle (বৃত্ত)
| **Property**      | **Formula**              | **Notes**                      |
| ----------------- | ------------------------ | ------------------------------ |
| **Circumference** | $C = 2\pi r$ or  $\pi d$ | \( r \) = radius, \( d = 2r \) |
| **Area**          | \( $A = \pi r^2$ \)      | \( \pi \approx 3.1416 \)       |
| **Diameter**      | \( $d = 2r$ \)           | Straight line through center   |

- **Example**: Radius = 5:
  - Circumference = $2 \times 3.14 \times 5 = 31.4$ 
  - Area = $3.14 \times 5^2 = 78.5$ 

#### 3. Rectangle (আয়তক্ষেত্র)
| **Property**  | **Formula**      | **Notes**                         |
| ------------- | ---------------- | --------------------------------- |
| **Area**      | A = $l \times w$ | \( l \) = length, \( w \) = width |
| **Perimeter** | P =$2(l + w)$    | Opposite sides equal              |

- **Example**: \( l = 6, w = 4 \):
  - Area = \( $6 \times 4$ = 24 \)
  - Perimeter = \( 2(6 + 4) = 20 \)

#### 4. Square (বর্গক্ষেত্র)
| **Property**  | **Formula**     | **Notes**             |
| ------------- | --------------- | --------------------- |
| **Area**      | \( $A = s^2$ \) | \( s \) = side length |
| **Perimeter** | \( $P = 4s$ \)  | All sides equal       |

- **Example**: \( s = 3 \):
  - Area = \( 3^2 = 9 \)
  - Perimeter = \( 4 \times 3 = 12 \)

---

### Algebraic Identities and Equations

#### 1. Basic Identities
These are shortcuts for expanding or factoring expressions.

| **Identity**         | **Formula**                             | **Use Case**                      |
| -------------------- | --------------------------------------- | --------------------------------- |
| $( (a + b)^2 )$      | $( a^2 + 2ab + b^2 )$                   | Squaring a binomial               |
| $( (a - b)^2 )$      | $( a^2 - 2ab + b^2 )$                   | Squaring a difference             |
| $( (a + b)(a - b) )$ | $( a^2 - b^2)$                          | Difference of squares             |
| $( (a + b + c)^2 )$  | $( a^2 + b^2 + c^2 + 2ab + 2ac + 2bc )$ | Squaring a trinomial              |
| $( (a + b)^3 )$      | $( a^3 + 3a^2b + 3ab^2 + b^3 )$         | Cubing a binomial                 |
| $( (a - b)^3 )$      | $( a^3 - 3a^2b + 3ab^2 - b^3 )$         | Cubing a difference               |
| $( a^3 + b^3 )$      | $( (a + b)(a^2 - ab + b^2) )$           | Sum of cubes factorization        |
| $( a^3 - b^3)$       | $( (a - b)(a^2 + ab + b^2) )$           | Difference of cubes factorization |

- **Example**: Expand \( $(2 + 3)^2$ \):
  -  $(2 + 3)^2 = 2^2 + 2 \times 2 \times 3 + 3^2 = 4 + 12 + 9 = 25$

#### 2. Quadratic Equations
Form: $( ax^2 + bx + c = 0)$
- **Roots**: Use the quadratic formula:

  $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
  
  - $( b^2 - 4ac )$ (discriminant):
    - \( > 0 \): Two real, distinct roots
    - \( = 0 \): One real root (repeated)
    - \( < 0 \): No real roots (complex)

- **Example**: Solve $( 2x^2 - 4x - 6 = 0 )$:
  - $( a = 2, b = -4, c = -6 \)$
  - Discriminant = $( (-4)^2 - 4 \times 2 \times (-6) = 16 + 48 = 64)$
  - Roots = $( \frac{4 \pm \sqrt{64}}{4} = \frac{4 \pm 8}{4} )$
    - $( x = \frac{12}{4} = 3 )$
    - \($x = \frac{-4}{4} = -1$ \)
  - Solution: \( $x = 3, -1$ \)

#### 3. Cubic Equations
Form: $( ax^3 + bx^2 + cx + d = 0 )$
- **Solving**: Less common in basic exams, but key methods include:
  1. **Factorization**: Find a root (e.g., by trial), then factor into a quadratic.
  2. **Cardano’s Method**: Advanced, not typically exam-level.
- **Example**: Solve \( $x^3 - 6x^2 + 11x - 6 = 0$ ):
  - Try $( x = 1 ): ( 1 - 6 + 11 - 6 = 0$ ) (works).
  - Factor: $( (x - 1)(x^2 - 5x + 6) = 0 )$
  - Solve quadratic: $( x^2 - 5x + 6 = 0 )$
    - $( (x - 2)(x - 3) = 0 )$
    - $( x = 2, 3 )$
  - Roots: $( x = 1, 2, 3 )$

---

### Exam Prep Notes (Obsidian-Friendly)

#### Geometry
- **Triangle Trick**: 
  - General: \( $\frac{1}{2} \times \text{base} \times \text{height}$ \)
  - Equilateral: \( $\frac{\sqrt{3}}{4} \times \text{side}^2 ) (think "root 3 over 4")$
  - Right: Pythagoras \( $a^2 + b^2 = c^2 ), area ( \frac{1}{2} ab$ \)
  - Heron’s: \( $s = \frac{\text{all sides}}{2} ), then ( \sqrt{s(s-a)(s-b)(s-c)}$ \)
- **Circle**: \( $\pi r^2 ) (area), ( 2\pi r ) (perimeter)—memorize ( \pi \approx 3.14$ \).
- **Rectangle/Square**: \( $l \times w ) or ( s^2$ \), perimeter doubles or quadruples sides.

#### Algebra
- **Identities**: 
  - $( (a + b)^2 = a^2 + 2ab + b^2 )$ (square, double cross, square)
  - $( a^2 - b^2 = (a + b)(a - b) )$ (difference of squares)
  - $( (a + b)^3 )$ = cube + 3 times square-cross + cube
- **Quadratic**: $( x = \frac{-b \pm \sqrt{\text{discriminant}}}{2a} )—check ( b^2 - 4ac )$.
- **Cubic**: Test roots (1, -1, 2), factor, solve the rest.

---

This covers the basics you’ll likely need for exams like BCS or OS-related math sections. Let me know if you want more shapes (e.g., trapezoid, sphere) or deeper equation examples!


1. দুই অংক বিশিষ্ট একটি সংখ্যার অঙ্কদ্বয়ের সমষ্টি ৯। অংকদ্বয় স্থান পরিবর্তন করলে যে সংখ্যা পাওয়া যায় তা প্রদত্ত সংখ্যা হতে ৪৫ কম। সংখ্যাটি কত #math/5 
	assume that the number is $xy$
		$therefore$  $x+y = 9$
		if we reverse the number  it becomes $yx$
	
	now according to the qustion the difference of xy-45 = yx 
		$therefore$  $10x+y - 45 =10y+x$
		$9x-9y=45$
		$x-y=5$
		$9-y-y=5$  $\to$   $9-2y=5$  $\to$ $4=2y$  $\to$ $y=2$
		$x= 7$
		so the number is 72
 ^069ddc
5. 