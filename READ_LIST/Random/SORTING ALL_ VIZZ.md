### Summary of Sorting Algorithms

  

Below is a concise summary of each algorithm with its steps:

  

- **Bubble Sort** [[psudo codes#1. Bubble sort|BS..]]

	Initial Array: [3, 2, 5, 0, 1, 8, 7, 6, 9, 4]
	1. **Pass 1:**
	    - [3, 2] → Swap: [2, 3, 5, 0, 1, 8, 7, 6, 9, 4]      
	    - [3, 5] → No swap.
	    - [5, 0] → Swap: [2, 3, 0, 5, 1, 8, 7, 6, 9, 4]
	    - [5, 1] → Swap: [2, 3, 0, 1, 5, 8, 7, 6, 9, 4]
	    - [5, 8] → No swap.
	    - [8, 7] → Swap: [2, 3, 0, 1, 5, 7, 8, 6, 9, 4]
	    - [8, 6] → Swap: [2, 3, 0, 1, 5, 7, 6, 8, 9, 4]
	    - [8, 9] → No swap.
	    - [9, 4] → Swap: [2, 3, 0, 1, 5, 7, 6, 8, 4, 9]
	    - **Result:** [2, 3, 0, 1, 5, 7, 6, 8, 4, 9] (9 at end).
	  
	2. **Pass 2:**
	    - [2, 3] → No swap.
	    - [3, 0] → Swap: [2, 0, 3, 1, 5, 7, 6, 8, 4, 9]
	    - [3, 1] → Swap: [2, 0, 1, 3, 5, 7, 6, 8, 4, 9]
	    - [3, 5] → No swap.
	    - [5, 7] → No swap.
	    - [7, 6] → Swap: [2, 0, 1, 3, 5, 6, 7, 8, 4, 9]
	    - [7, 8] → No swap.
	    - [8, 4] → Swap: [2, 0, 1, 3, 5, 6, 7, 4, 8, 9]
	    - **Result:** [2, 0, 1, 3, 5, 6, 7, 4, 8, 9] (8 at second-to-last).
	      
	  
	3. **Pass 3:**
	    - [2, 0] → Swap: [0, 2, 1, 3, 5, 6, 7, 4, 8, 9]
	    - [2, 1] → Swap: [0, 1, 2, 3, 5, 6, 7, 4, 8, 9]
	    - [2, 3] → No swap.
	    - [3, 5] → No swap.
	    - [5, 6] → No swap.
	    - [6, 7] → No swap.
	    - [7, 4] → Swap: [0, 1, 2, 3, 5, 6, 4, 7, 8, 9]
	    - **Result:** [0, 1, 2, 3, 5, 6, 4, 7, 8, 9] (7 at third-to-last).
	  
	5. **Pass 4:**
	    - [0, 1] → No swap.
	    - [1, 2] → No swap.
	    - [2, 3] → No swap.
	    - [3, 5] → No swap.
	    - [5, 6] → No swap.
	    - [6, 4] → Swap: [0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
	    - **Result:** [0, 1, 2, 3, 5, 4, 6, 7, 8, 9] (6 at fourth-to-last).
	      
	    
	  
	7. **Pass 5:**
	    - [0, 1] → No swap.
	    - [1, 2] → No swap.
	    - [2, 3] → No swap.
	    - [3, 5] → No swap.
	    - [5, 4] → Swap: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	    - **Result:** [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (fully sorted).

  
- **Insertion Sort on  **[7, 2, 5, 4, 1]**.  [[psudo codes#2. Insertion Sort|psudo.]]
    #### Initial Array
	We start with: **[7, 2, 5, 4, 1]**.
	#### Step 1: Insert 2
	- **Sorted portion:** [7] (the first element is considered sorted by default).
	  
	- **Current element:** ==2 (the second element).==
	  
	- **Process:**
    - Compare 2 with 7. Since 2 < 7, shift 7 to the right.
    - There are no more elements to compare, so insert 2 at the beginning.
      
	- **Result:** **[2, 7, 5, 4, 1]**.	  
	
	
	#### Step 2: Insert 5
	
	- **Sorted portion:** [2, 7] (the first two elements are now sorted).
	- **Current element:** ==5 (the third element).==
	
	- **Process:**
    - Compare 5 with 7. Since 5 < 7, shift 7 to the right.  
    - Compare 5 with 2. Since 5 > 2, insert 5 after 2.
      
	- **Result:** **[2, 5, 7, 4, 1]**.
	
	#### Step 3: Insert 4
	- **Sorted portion:** [2, 5, 7] (the first three elements are sorted).
	- **Current element:** 4 (the fourth element).
  
	- **Process:**
    - Compare 4 with 7. Since 4 < 7, shift 7 to the right. 
    - Compare 4 with 5. Since 4 < 5, shift 5 to the right.
    - Compare 4 with 2. Since 4 > 2, insert 4 after 2.
     
	- **Result:** **[2, 4, 5, 7, 1]**.
  

	#### Step 4: Insert 1
	- **Sorted portion:** [2, 4, 5, 7] (the first four elements are sorted).
	  
	- **Current element:** 1 (the fifth element).	  
	- **Process:**
    - Compare 1 with 7. Since 1 < 7, shift 7 to the right.
    - Compare 1 with 5. Since 1 < 5, shift 5 to the right.
    - Compare 1 with 4. Since 1 < 4, shift 4 to the right.
    - Compare 1 with 2. Since 1 < 2, shift 2 to the right.
    - There are no more elements to compare, so insert 1 at the beginning.
      
	- **Result:** **[1, 2, 4, 5, 7]**.



- **Selection Sort on [4, 5, 3, 2]:**  [[psudo codes#3. Selection Sort|psudo]]
    - **Initial:** [4, 5, 3, 2]
	- **Step 1 (First Selection):** Find minimum in [4, 5, 3, 2], which is 2. Swap 2 with 4. Result: [2, 5, 3, 4].
	- **Step 2 (Second Selection):** Unsorted portion is [5, 3, 4]. Minimum is 3. Swap 3 with 5. Result: [2, 3, 5, 4].
	- **Step 3 (Third Selection):** Unsorted portion is [5, 4]. Minimum is 4. Swap 4 with 5. Result: [2, 3, 4, 5].
    
  
- **Merge Sort on [4, 2, 3, 1]:**
    - Initial: [4, 2, 3, 1]
      
    - After merging pairs: [2, 4, 1, 3]
      
    - After merging halves: [1, 2, 3, 4]
      
    
  
- **Quick Sort on  [3,2,5,0,1,8,7,6,9,4]
	
	 take pivtot 4 
	 and 2 rules like 
      ![[sort_quick.png]]
		say 2 pointer are there { ==p,q== }  ||   ==p at 0== \[3\] index and **==q at -1:==**
		now we will ==increment p== **each step**
		and only do any action **if & only if** current elm is ==less than pivot== else ==pass==
		if thats the case ( [p] <pivot ):
			increase q+1 and check that this [q] > [p] : 
				only then change 
			else: if **the index is same** ==pass==
		3<= 4 || p=0 > q+1 =0 || *BUT* p=q (same index)  > ==PASS==
		2<= 4 || p=1 > q = 1 || same index >> PASS
		5 >= 4 || p=2 ==PASS==
		0 <= 4 || p=3, q+1=2 || \[2\]=5 \[3\]=0 : swap    \\\ \[3,2,==0,5==,1,8,7,6,9,4] 
		1 <= 4 || p=4, q+1=3 || \[3\]=5 \[4\]=1 : swap    \\\ \[3,2,0,==1,5==, 8,7,6,9,4] 
		................... upto 9 no change: 
		4 <= 4 || p= 9 and q+1 = 4 || \[4] = 5 \[9]=4 : swap   \\ \[  3,2,0,1 ] 4, \[ 8,7,6,9,5] 
		NOW  DO RECURSIVELY FOR BOTH ==LEFT== AND ==RIGHT==
  
- **Heap Sort on [5, 3, 4, 2]:**
    - Initial: [5, 3, 4, 2]
      
    - After first swap and heapify: [4, 3, 2, 5]
      
    - After second swap and heapify: [3, 2, 4, 5]
      
    - After third swap: [2, 3, 4, 5]