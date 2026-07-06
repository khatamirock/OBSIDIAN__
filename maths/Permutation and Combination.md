
#### 1. In how many different ways can the letters of the word 'CORPORATION' be arranged so that the vowels always come together?

Let's solve this step by step:

1. First, let's count the letters in 'CORPORATION': • Total letters = 11 • Vowels = O, O, A, I, O (5 vowels) • Consonants = C, R, P, R, T, N (6 consonants)
    
2. We'll first group the vowels together as one unit: • Now we have 7 units to arrange:
    
    - VOWELS (treated as one unit)
    - C, R, P, R, T, N (individual consonants)
3. Let's calculate the number of arrangements: • Total arrangements = (Number of ways to arrange 7 units) × (Number of ways to arrange vowels internally)
    
4. Number of ways to arrange 7 units = 7! • But we have repeated consonants (2 R's) • So we divide by 2! to remove duplicate arrangements
    
    $\frac{7!}{2!}$
    
5. Vowel arrangements: • 5 vowels with repeats (3 O's) • 5! ÷ (3!)
    
6. Final calculation: (7! ÷ 2!) × (5! ÷ 3!)
    
#### 2. Out of 7 consonants and 4 vowels, how many words of 3 consonants and 2 vowels can be formed?


#### 1. In how many different ways can the letters of the word 'CORPORATION' be arranged so that the vowels always come together?

Let's solve this step by step:

1. First, let's count the letters in 'CORPORATION': • Total letters = 11 • Vowels = O, O, A, I, O (5 vowels) • Consonants = C, R, P, R, T, N (6 consonants)
    
2. We'll first group the vowels together as one unit: • Now we have 7 units to arrange:
    
    - VOWELS (treated as one unit)
    - C, R, P, R, T, N (individual consonants)
3. Let's calculate the number of arrangements: • Total arrangements = (Number of ways to arrange 7 units) × (Number of ways to arrange vowels internally)
    
4. Number of ways to arrange 7 units = 7! • But we have repeated consonants (2 R's) • So we divide by 2! to remove duplicate arrangements
    
    $\frac{7!}{2!}$
    
5. Vowel arrangements: • 5 vowels with repeats (3 O's) • 5! ÷ (3!)
    
6. Final calculation: (7! ÷ 2!) × (5! ÷ 3!)
    
#### 2. Out of 7 consonants and 4 vowels, how many words of 3 consonants and 2 vowels can be formed?

##### Step 1: Choose the consonants
- You have 7 consonants available.
- You need to select 3 of them.
- The number of ways to choose 3 consonants from 7 is given by the combination formula ( $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ ), where order doesn’t matter yet.
- So, ( $\binom{7}{3} = \frac{7!}{3!(7-3)!} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35$ ).

##### Step 2: Choose the vowels
- You have 4 vowels available.
- You need to select 2 of them.
- The number of ways to choose 2 vowels from 4 is:
- $( \binom{4}{2} = \frac{4!}{2!(4-2)!} = \frac{4 \times 3}{2 \times 1} = 6 )$

##### Step 3: Arrange the 5 letters
- After choosing 3 consonants and 2 vowels, you have a total of 5 distinct letters (assuming all consonants and vowels are unique).
- A "word" implies a sequence, so we need to arrange these 5 letters in all possible orders.
- The number of ways to arrange 5 distinct letters is $( 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120 )$.

##### Step 4: Combine the choices and arrangements
- First, you choose the consonants: 35 ways.
- Then, you choose the vowels: 6 ways.
- Then, you arrange the 5 chosen letters: 120 ways.
- Total number of words = $( \binom{7}{3} \times \binom{4}{2} \times 5! = 35 \times 6 \times 120 ).$

##### Calculation
- $( 35 \times 6 = 210 ).$
- $( 210 \times 120 = 25,200 )$

So, the total number of possible words is **25,200**.


#### 3. How many 3-digit numbers can be formed from the digits 2, 3, 5, 6, 7 and 9, which are divisible by 5 and none of the digits is repeated?

take ==5== at ==unit place== so we are left with ==2== place
choose 2 digit from the available 5 digits 
(5C2) and shift them in between 2!   $\to$  5c2 \* 2!   = 20 

**another way :**
Number of permutations of 5 digits taken 2 at a time:
$P(5,2)=5×4=20.$




#### 3.   A box contains 2 white balls, 3 black balls and 4 red balls. In how many ways can 3 balls be drawn from the box, if at least one black ball is to be included in the draw?

We may have(1 black and 2 non-black) or (2 black and 1 non-black) or (3 black).


| ![](https://www.indiabix.com/_files/images/aptitude/1-sym-tfr.gif) Required number of ways | = (3C1 x 6C2) + (3C2 x 6C1) + (3C3) |  = 64        |
| ------------------------------------------------------------------------------------------ | ----------------------------------- | ------ |
#### 4.   In how many different ways can the letters of the word 'DETAIL' be arranged in such a way that the vowels occupy only the odd positions?



#### 5.    In how many different ways can the letters of the word 'OPTICAL' be arranged so that the vowels always come together?

thre are 3 vowels (OIA) so we got 5 letters now
so we can arrange them in 5! way 
and (OIA) can arrange inbetween them in 3! way
so , total = 5! \* 3!  = 720

