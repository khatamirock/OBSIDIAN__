### **Solution for Prob -3 & more**
 
#### **Step 1: Propagation Time**

==Propagation time is the time it takes for a **signal** to travel from the sender to the receiver.==

Formula: **Propagation Time** = Distance / Signal Speed

- **Distance:** 12,000 km = 12,000,000 meters
- **Signal Speed:** 2.4 x 10⁸ m/s

Propagation Time = 12,000,000 / (2.4 x 10⁸)  
Propagation Time = **0.05 seconds (50 milliseconds)**

---

#### **Step 2: Transmission Time** (==Avoidable cause so tiny!==)

==Transmission time is the time it takes to send the **data** over the network.==

Formula: ==**Transmission Time** = Message Size / Bandwidth==

**==use only if they asked transmission time==**

- **Message Size:** 2.5 kB = 2.5 x 1024 bytes = 2560 bytes = 2560 x 8 bits = 20,480 bits
- **Bandwidth:** 1 Gbps = 1 x 10⁹ bits per second

Transmission Time = 20,480 / (1 x 10⁹)  
Transmission Time = **0.00002048 seconds (20.48 microseconds)**

---

#### **Step 3: Total Time**
**==Propagation time is independent of message size (e.g., 2.5-kbyte email). It only depends on distance and propagation speed.==**

The total time is the sum of the propagation time and the transmission time:

Total Time = Propagation Time + Transmission Time (==useless== for now) 
Total Time = 0.05 + 0.00002048  
Total Time = **0.05002048 seconds (approximately 50 milliseconds)** 

---

#### **Answer:**

The propagation time is approximately **50 milliseconds**.

---

#### **More Examples**

1. **Example 1:** What is the ==propagation== time for a 1000 km distance if the signal speed is 3 x 10⁸ m/s?

- Distance = 1,000,000 m
- Signal Speed = 3 x 10⁸ m/s
- Propagation Time = 1,000,000 / (3 x 10⁸) = **0.0033 seconds (3.33 milliseconds)**

---

2. **Example 2:** What is the ==transmission== time for a 1 MB file over a network with 100 Mbps bandwidth?

- File Size = 1 MB = 1 x 1024 x 1024 bytes = 8,388,608 bits
- Bandwidth = 100 Mbps = 100 x 10⁶ bits/s
- Transmission Time = 8,388,608 / (100 x 10⁶) = **0.08388 seconds (83.88 milliseconds)**

---

3. **Example 3:** What is the total time for a 5 kB file to be transmitted over a 1 Gbps network, given a propagation distance of 5000 km at a signal speed of 2 x 10⁸ m/s?

- Propagation Time = Distance / Signal Speed  
    Distance = 5000 km = 5,000,000 m  
    Signal Speed = 2 x 10⁸ m/s  
    Propagation Time = 5,000,000 / (2 x 10⁸) = **0.025 seconds (25 ms)**
    
- Transmission Time = File Size / Bandwidth  
    File Size = 5 kB = 5 x 1024 bytes = 40,960 bits  
    Bandwidth = 1 Gbps = 1 x 10⁹ bits/s  
    Transmission Time = 40,960 / (1 x 10⁹) = **0.000041 seconds (41 microseconds)**
    
- Total Time = Propagation Time + Transmission Time  
    Total Time = 0.025 + 0.000041 = **0.025041 seconds (25.041 milliseconds)**
    

---


### **Shanon Nd Nyquist Problems**

We are asked to calculate the **maximum data rate** of a channel with:

- **Bandwidth (B):** 200 kHz
- **Number of signaling levels (M):** 4

To solve this, we use **Shannon’s Channel Capacity formula** or **Nyquist’s formula**, depending on the context.

---

##### **1. Use Nyquist's Formula (for noiseless channels):**

The formula for maximum data rate in a noiseless channel is:

${Maximum Data Rate} = 2 \times B \times \log_2(M)$

Where:

- B = Bandwidth (in Hz)
- M = Number of signaling levels

##### Step-by-Step Solution:

1. Bandwidth B=200,000B = 200,000 Hz
2. Signaling levels M=4M = 4  
    $log⁡2(M)=log⁡2(4)=2\log_2(M) = \log_2(4) = 2$

$Maximum Data Rate = 2 \times 200,000 \times 2 = 800,000 \, \text{bps (800 Kbps)}$

---

**Correct Answer: (b) 800 Kbps**

---

#### **Why Not Use Shannon’s Formula?**

- Shannon’s formula $(C=Blog⁡2(1+S/N)C = B \log_2(1 + S/N))$ accounts for noise. Since noise isn't mentioned here, Nyquist's formula is more appropriate.

---

#### **More Examples:**

##### **Example 1: What is the data rate of a channel with a bandwidth of 1 MHz and 8 signaling levels?**

- B=1,000,000B = 1,000,000 Hz
- $M=8M = 8, so log⁡2(M)=log⁡2(8)=3\log_2(M) = \log_2(8) = 3$

$\text{Data Rate} = 2 \times B \times \log_2(M) = 2 \times 1,000,000 \times 3 = 6,000,000 \, \text{bps (6 Mbps)}$

---

##### **Example 2: Calculate the maximum data rate for a channel with 500 KHz bandwidth and 16 levels.**

- B=500,000B = 500,000 Hz
- $M=16M = 16, so log⁡2(M)=log⁡2(16)=4\log_2(M) = \log_2(16) = 4$

$\text{Data Rate} = 2 \times B \times \log_2(M) = 2 \times 500,000 \times 4 = 4,000,000 \, \text{bps (4 Mbps)}$

---

##### **Example 3: What is the data rate for a 50 kHz bandwidth channel with 2 signaling levels?**

- B=50,000B = 50,000 Hz
- M=2M = 2, so log⁡2(M)=log⁡2(2)=1\log_2(M) = \log_2(2) = 1

$\text{Data Rate} = 2 \times B \times \log_2(M) = 2 \times 50,000 \times 1 = 100,000 \, \text{bps (100 Kbps)}$

---

##### **Example 4: Calculate the data rate for a channel with 300 KHz bandwidth and 32 levels.**

- B=300,000B = 300,000 Hz
- $M=32M = 32, so log⁡2(M)=log⁡2(32)=5\log_2(M) = \log_2(32) = 5$

$\text{Data Rate} = 2 \times B \times \log_2(M) = 2 \times 300,000 \times 5 = 3,000,000 \, \text{bps (3 Mbps)}$

---
When dealing with a **noisy channel**, we calculate the **maximum data rate (channel capacity)** using **==Shannon's Capacity Formula==**:

$C=B×log⁡2(1+SNR)C = B \times \log_2(1 + \text{SNR})$

Where:

- **C** = Channel Capacity (in bits per second, bps)
- **B** = Bandwidth of the channel (in Hz)
- **SNR** = Signal-to-Noise Ratio (unitless, often given in dB)

---
#### ==Shanon Problems  (Noisy Channel)==
#### **Example 1: Channel with 300 kHz bandwidth and SNR = 30 dB**

1. Convert **SNR (in dB)** to unitless form:

${SNR (unitless)} = 10^{\text{SNR(dB)} / 10} = 10^{30 / 10} = 10^3 = 1000$

2. Plug into Shannon's formula:

    $C = 300,000 \times \log_2(1 + 1000)$
  
   $C=300,000×log⁡2(1001)C = 300,000 \times \log_2(1001)$

    $Approximate: log⁡2(1001)≈9.97\log_2(1001) \approx 9.97$
	    $C = 300,000 \times 9.97 \approx 2,991,000 \, \text{bps (2.99 Mbps)}$


---

#### **Example 2: 1 MHz bandwidth, SNR = 20 dB**

3. Convert **SNR (dB)** to unitless:    
    $SNR=1020/10=102=100\text{SNR} = 10^{20 / 10} = 10^2 = 100$

4. Plug into Shannon's formula:
	$C=1,000,000×log⁡2(1+100)C = 1,000,000 \times \log_2(1 + 100) C=1,000,000×log⁡2(101)C = 1,000,000 \times \log_2(101)$

$Approximate: log⁡2(101)≈6.66\log_2(101) \approx 6.66$	
	$C=1,000,000×6.66≈6,660,000 bps (6.66 Mbps)C = 1,000,000 \times 6.66 \approx 6,660,000 \, \text{bps (6.66 Mbps)}$


---

#### **Example 3: 500 kHz bandwidth, SNR = 10 dB**

5. Convert **SNR (dB)** to unitless:
    
$$
    SNR=1010/10=101=10\text{SNR} = 10^{10 / 10} = 10^1 = 10
$$
6. Plug into Shannon's formula:
    
$$
    C=500,000×log⁡2(1+10)C = 500,000 \times \log_2(1 + 10) C=500,000×log⁡2(11)C = 500,000 \times \log_2(11)
$$
    
$$
    Approximate: log⁡2(11)≈3.46\log_2(11) \approx 3.46
$$
    

    $C=500,000×3.46≈1,730,000 bps (1.73 Mbps)C = 500,000 \times 3.46 \approx 1,730,000 \, \text{bps (1.73 Mbps)}$


---

#### **Example 4: 2 MHz bandwidth, SNR = 40 dB**

7. Convert **SNR (dB)** to unitless:
    

 $SNR=1040/10=104=10,000\text{SNR} = 10^{40 / 10} = 10^4 = 10,000$

8. Plug into Shannon's formula:
    

    $C=2,000,000×log⁡2(1+10,000)C = 2,000,000 \times \log_2(1 + 10,000) C=2,000,000×log⁡2(10,001)C = 2,000,000 \times \log_2(10,001)$

    $Approximate: log⁡2(10,001)≈13.29\log_2(10,001) \approx 13.29$
    
    $C=2,000,000×13.29≈26,580,000 bps (26.58 Mbps)C = 2,000,000 \times 13.29 \approx 26,580,000 \, \text{bps (26.58 Mbps)}$


---

#### **Example 5: 100 kHz bandwidth, SNR = 15 dB**

9. Convert **SNR (dB)** to unitless:
    

$SNR=1015/10=31.62\text{SNR} = 10^{15 / 10} = 31.62$

10. Plug into Shannon's formula:
    

    $C=100,000×log⁡2(1+31.62)C = 100,000 \times \log_2(1 + 31.62) C=100,000×log⁡2(32.62)C = 100,000 \times \log_2(32.62)$

    

    $Approximate: log⁡2(32.62)≈5.03\log_2(32.62) \approx 5.03$

    $C=100,000×5.03≈503,000 bps (503 Kbps)C = 100,000 \times 5.03 \approx 503,000 \, \text{bps (503 Kbps)}$



 ---
 


### Probability:
#### 1.
To find  P(A∪B)P(A $\cup$ B), we use the **union formula** in probability:

P(A $\cup$ B) = P(A) + P(B) - P(A $\cap$ B)

We are given:

- P(A)=0.6P(A) = 0.6
- P(B)=0.4P(B) = 0.4
- P(B | A) = 0.2 (Conditional probability of B given A)

From the definition of conditional probability:

P(B∣A)=$P(B | A)$ = $\frac{P(A \cap B)}{P(A)}$

Substituting the given values:

$0.2=P(A∩B)0.60.2 = \frac{P(A \cap B)}{0.6}$ 
$P(A \cap B) = 0.2 \times 0.6 = 0.12$

Now, applying the union formula:

$P(A \cup B) = 0.6 + 0.4 - 0.12$
$P(A \cup B) = 0.88$

##### **Final Answer:**

$P(A \cup B) = 0.88$

#### 2. Combination and Perm example for Math 11
##### 🔍 Explanation:

We need to select **4 books out of 10**, but **2 specific books must always be left out**.


11. Since 2 books are always left out, we are left with:  
    **10 - 2 = 8 books**.
12. Now, we need to **choose 4 books** from these **8 books**.
13. The number of ways to do this is given by the **combination formula**: $nCr=n!r!(n−r)!^nC_r = \frac{n!}{r!(n-r)!}$ Here, **n = 8** and **r = 4**, 
14. so . $8C_4 = \frac{8!}{4!(8-4)!}$ =$\frac{8!}{4!4!} = \frac{8 × 7 × 6 × 5}{4 × 3 × 2 × 1}$ = 70

✅ **Final Answer: 70 ways**


---

##### ✨ **More Similar Questions (Practice Problems)**

###### ✅ **Selection Problems (Similar to Given Question)**

15. **In how many ways can 5 students be selected from a class of 12 if 2 specific students must always be selected?**  
    ➝ Solution: Choose 3 more from the remaining 10.
    
16. **A committee of 4 members is to be formed from 10 people, but 2 specific people must always be included. How many ways can this be done?**  
    ➝ Solution: Choose 2 more from the remaining 8.
    

---

###### ✅ **Permutation Problems (When Order Matters)**

17. **In how many ways can 3 prizes be distributed among 7 students if no student can receive more than one prize?**  
    ➝ Use **P(n, r) = nPr = n! / (n-r)!**
    
18. **How many different ways can 5 books be arranged on a shelf if 2 books must always be together?**  
    ➝ Treat the 2 books as a single unit, then arrange the remaining ones.
    

---

###### ✅ **Combination with Constraints**

19. **In how many ways can a cricket team of 11 players be selected from 15 players if 3 specific players must always be included?**  
    ➝ Choose 8 more from the remaining 12.
    
20. **In how many ways can 3 students be chosen from a group of 9 if 2 specific students cannot be selected?**  
    ➝ Remove the 2 and choose from the remaining 7.
    

---
##### **1. Arranging Letters of "DIGITAL" with Vowels Together**

###### **Step 1: Identify Total Letters & Vowels**

- The word **"DIGITAL"** has **7** letters: **D, I, G, I, T, A, L**
- **Vowels** = {I, I, A}
- **Consonants** = {D, G, T, L}

###### **Step 2: Treat Vowels as a Single Unit**

Since the vowels must stay together, we treat **(IIA) as one unit**.  
Now, the elements to arrange:

- **Consonants: D, G, T, L**
- **Vowel group (IIA) as a single unit**

So, we have **5 elements to arrange**:  
**(D, G, T, L, [IIA])**

###### **Step 3: Arrange These Units**

- The **5 elements** can be arranged in: 5!=5×4×3×2×1=1205! = 5 × 4 × 3 × 2 × 1 = 120

###### **Step 4: Arrange the Vowels Inside Their Unit**

- The vowels **(IIA)** can be arranged among themselves: 3!2!=3×2×12×1=3\frac{3!}{2!} = \frac{3 × 2 × 1}{2 × 1} = 3

###### **Final Calculation**

120×3=360120 \times 3 = 360

✅ **Answer: 360 ways**

---

##### **2. Distributing 3 Prizes Among 7 Students (No Student Receives More Than One Prize)**

###### **Step 1: Identify the Type of Selection**

- Since the **prizes are distinct**, **order matters** (because winning Prize A is different from winning Prize B).
    
- **No repetition** (one student can't get more than one prize).
    
- This is a **permutation problem**, calculated as:
    
    P(n,r)=n!(n−r)!P(n, r) = \frac{n!}{(n-r)!}

###### **Step 2: Apply Formula**

P(7,3)=7!(7−3)!=7!4!P(7, 3) = \frac{7!}{(7-3)!} = \frac{7!}{4!}

Expanding factorials:

7×6×5×4!4!=7×6×5=210\frac{7 × 6 × 5 × 4!}{4!} = 7 × 6 × 5 = 210

✅ **Answer: 210 ways**
##### **Key Takeaways** 🚀

✔ **Combination (nCr) → When order doesn’t matter**  
✔ **Permutation (nPr) → When order matters**  
✔ **Factorial simplifications help save time**  
✔ **Identify constraints carefully**  
✔ **Practice different variations**

This method will help you quickly solve these problems in exams with confidence! ✅🔥



### Statistics
#### 1. 
To find the **median** when the **mode** and **mean** are given, we can use **Empirical Relationship of Central Tendency**:

$Mean−Mode=3(Mean−Median)\text{Mean} - \text{Mode} = 3 (\text{Mean} - \text{Median})$

Given:

- **Mode** = 7
- **Mean** = 8

Substituting into the formula:

$8−7=3(8−Median)8 - 7 = 3 (8 - \text{Median}) 1=3(8−Median)1 = 3 (8 - \text{Median})$ $13=8−Median\frac{1}{3} = 8 - \text{Median}$
$Median=8−13=243−13=233=7.67\text{Median} = 8 - \frac{1}{3} = \frac{24}{3} - \frac{1}{3} = \frac{23}{3} = 7.67$

##### **Final Answer:**

$Median≈7.67\text{Median} \approx 7.67$







### Trig

#### Basic Formulas
 
##### **Basic Identities**

21. $\sin^2 A + \cos^2 A = 1$
22. $1 + \tan^2 A = \sec^2 A$
23. $1 + \cot^2 A = \csc^2 A$

##### **Sum and Difference Formulas**

24. $\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$
25. $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$

##### **Product-to-Sum and Sum-to-Product**

26. $\sin A + \cos A = \sqrt{2} \sin (A + 45^\circ)$
27. $2 \sin A \cos B = \sin(A + B) + \sin(A - B)$

 





### MISC
#### 1. If a: b = 3:4, b:c = 7:9, c:d = 5:7, Evaluate a:d?
We multiply the given ratios together to find a:d:

$\frac{a}{b} \times \frac{b}{c} \times \frac{c}{d} = \frac{a}{d}​$

Substituting the given values:

$\frac{3}{4} \times \frac{7}{9} \times \frac{5}{7}$
