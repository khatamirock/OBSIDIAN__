### 🧠 Intuitive Algorithm for Insertion Sort

**Algorithm: Insertion_Sort(A, n)**  
**Input:** An array `A` of `n` elements  
**Output:** Sorted array `A` in ascending order

---

1. **Start**
    
2. **For** `i ← 1` **to** `n − 1` **do**  
      a. Set `key ← A[i]`  
      b. Set `j ← i − 1`  
      c. **While** `j ≥ 0` **and** `A[j] > key` **do**  
        i. Move `A[j]` one position ahead → `A[j + 1] ← A[j]`  
        ii. Decrease `j ← j − 1`  
      d. Insert the `key` into the correct place → `A[j + 1] ← key`
    
3. **End For**
    
4. **Stop**
    

---

### 🧩 Example:

Let `A = [5, 2, 4, 6, 1, 3]`

After sorting → `A = [1, 2, 3, 4, 5, 6]`

---

### 🕒 Time Complexity:

- **Best case:** O(n) (Already sorted)
    
- **Worst case:** O(n²) (Reverse order)
    
- **Average case:** O(n²)
    

### 💾 Space Complexity:

- **O(1)** (In-place sorting)
    




## 🧠 Intuitive Algorithm for **Selection Sort**

**Algorithm: Selection_Sort(A, n)**  
**Input:** An array `A` of `n` elements  
**Output:** Sorted array `A` in ascending order

---

1. **Start**
    
2. **For** `i ← 0` **to** `n − 2` **do**  
      a. Assume the current index has the smallest element → `min_index ← i`  
      b. **For** `j ← i + 1` **to** `n − 1` **do**  
        If `A[j] < A[min_index]`, then update → `min_index ← j`  
      c. **If** `min_index ≠ i`, then swap → `A[i] ↔ A[min_index]`
    
3. **End For**
    
4. **Stop**
    

---

### 🧩 Example

Let `A = [5, 2, 4, 6, 1, 3]`

|Pass|Action|Result|
|---|---|---|
|1|Smallest is 1 → swap with 5|[1, 2, 4, 6, 5, 3]|
|2|Smallest from rest is 2 → stays|[1, 2, 4, 6, 5, 3]|
|3|Smallest from rest is 3 → swap with 4|[1, 2, 3, 6, 5, 4]|
|4|Smallest from rest is 4 → swap with 6|[1, 2, 3, 4, 5, 6]|
|5|Smallest from rest is 5 → stays|[1, 2, 3, 4, 5, 6]|

✅ Final sorted array → `[1, 2, 3, 4, 5, 6]`

---

### 🕒 Time Complexity:

- **Best case:** O(n²)
    
- **Worst case:** O(n²)
    
- **Average case:** O(n²)
    

### 💾 Space Complexity:

- **O(1)** (In-place sorting)


---

## 🫧 **Bubble Sort — Intuitive Algorithm**

**Algorithm:** `Bubble_Sort(A, n)`  
**Input:** Array `A` of `n` elements  
**Output:** Sorted array `A` in ascending order

---

### 🔹 Steps

1. **Start**
    
2. **For** `i ← 0` **to** `n − 2` **do**  
      a. **For** `j ← 0` **to** `n − i − 2` **do**  
        If `A[j] > A[j + 1]`, then **swap** → `A[j] ↔ A[j + 1]`  
      b. (Optional Optimization)  
        If no swaps occurred in this pass → **Stop early** (array already sorted)
    
3. **End For**
    
4. **Stop**
    

---

### 🧩 Example

Let `A = [5, 2, 4, 6, 1, 3]`

|Pass|Action|Result|
|---|---|---|
|1|Large values “bubble” up|[2, 4, 5, 1, 3, 6]|
|2|Continue bubbling|[2, 4, 1, 3, 5, 6]|
|3|More bubbling|[2, 1, 3, 4, 5, 6]|
|4|Almost done|[1, 2, 3, 4, 5, 6]|
|5|Fully sorted|[1, 2, 3, 4, 5, 6]|

✅ Final sorted array → `[1, 2, 3, 4, 5, 6]`

---

### 🕒 **Time Complexity**

- **Best case:** O(n) (when already sorted, if optimized)
    
- **Worst case:** O(n²)
    
- **Average case:** O(n²)
    

### 💾 **Space Complexity**

- **O(1)** (In-place sorting)
    

---
