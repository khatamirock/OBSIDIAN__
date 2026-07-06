Nice one 😎 — **Graph Theory** is a goldmine for trick MCQs. Teachers love setting questions where students trip over definitions, properties, or special cases.  
Here’s a **list of the most common “traps”** you’ll see in undergrad exams:

---

# 🎯 Graph Theory — Teacher Trap MCQs

### 1. **Basic Definitions**

- **Simple Graph vs Multigraph vs Pseudograph** → trick is on **self-loops** and **parallel edges**.
    
    - Simple graph: No self-loops, no multiple edges.
        
    - Multigraph: Parallel edges allowed, no self-loops.
        
    - Pseudograph: Both parallel edges and self-loops allowed.  
        👉 Trap: They’ll show a diagram and ask _“Is this simple?”_.
        

---

### 2. **Degree of Vertices**

- **Handshaking Lemma**: Sum of degrees = 2 × (edges).  
    👉 Trap: They give a graph with 5 vertices, ask _“Max possible edges?”_ → For simple graph: (n(n-1)/2).  
    👉 Trap: _“Can a graph have all vertices of odd degree?”_ → **No**, because sum of degrees must be even.
    

---

### 3. **Special Graphs**

- **Complete Graph ($K_n$):** Has (n(n-1)/2) edges.  
    👉 Trap: They’ll mix up with **Complete Bipartite Graph ($K_{m,n}$)** which has $(m \times n)$ edges.

        
- Any graph containing one of these as a **subgraph** (after subdivisions) is also non-planar.
- **Planar Graph:** Kuratowski’s theorem: (K_5) and (K_{3,3}) are not planar.  
    👉 Trap: They’ll ask if “K₄ is planar?” (Answer: **Yes**).
    - Two graphs are **NOT planar**:
	    - $K_5$​ → Complete graph on 5 vertices.
	    - $K_{3,3}$​ → Complete bipartite graph with 3 + 3 vertices.
    - Any graph containing one of these as a **subgraph** (after subdivisions) is also non-planar.

---

### 4. **Connectivity**

- Bridges (cut-edges) and Articulation points.  
    👉 Trap: Show a graph and ask “Which edge, if removed, disconnects the graph?”
    

---

### 5. **Euler vs Hamilton**

- **Eulerian Circuit:** Uses every edge exactly once. Condition: All vertices **MUST** HAVE ==even degree==.
	**Eulerian Path** (start & end different vertices): ==Exactly **2 vertices== have ==odd== degree** (the start & end).
- **Hamiltonian Circuit:** Visits every vertex exactly once. No simple test.  
    👉 Trap: They ask _“Which is easier to check?”_ (Euler).  
    👉 Trap: A ==graph can have Hamiltonian cycle but ⚠️not Eulerian==, and vice versa.
    

---

### 6. **Trees**

- **Tree properties:**
    
    - (n) vertices → (n-1) edges.
        
    - Always connected and acyclic.  
        👉 Trap: “A graph with n vertices and n–1 edges is always a tree?” → **Only if connected**.
        

---

### 7. **Graph Coloring**

- Chromatic number = minimum colors to color so no adjacent vertices share color.  
    👉 Trap: Bipartite graph chromatic number = **2**, unless it’s trivial (1 vertex → chromatic number = 1).
    - They’ll ask _“minimum number of colors sufficient for any graph with n vertices”_ → 
      Answer = **==n**== 
	- For ==_planar graphs_, the upper bound is **4**== (Four Color Theorem).

---

### 8. **Directed Graphs (Digraphs)**

- In-degree + Out-degree = total degree.  
    👉 Trap: Handshaking lemma applies separately: sum of in-degrees = sum of out-degrees = edges.
    

---

### 9. **Matrix Representations**

- Adjacency matrix vs Incidence matrix.  
    👉 Trap: Adjacency is **symmetric for undirected**, not for directed.  
    👉 Trap: They’ll ask about **space complexity**: adjacency matrix = O(n²), ==adjacency list = O(V+E).==
    

---

### 10. **Algorithms**

- **BFS/DFS:**  
    👉 Trap: BFS uses **queue**, DFS uses **stack/recursion**.  
    👉 Trap: Shortest path in _unweighted graph_ → BFS, not DFS.
    
- **Dijkstra’s:** Doesn’t work correctly with negative weights (they love this).
    
- **Bellman-Ford:** Handles negative weights.
    
- **Floyd-Warshall:** All-pairs shortest path.
    

---

✅ **Typical MCQ traps:**

- “Graph with 6 vertices, all degrees odd — possible?” → **No.**
    
- “Number of edges in K₄?” → 6.
    
- “Does bipartite graph contain odd cycle?” → **No.**
    
- “Chromatic number of cycle graph (C_n)?” → 2 if n even, 3 if n odd.
    

---

Do you want me to prepare a **ready-to-go MCQ set with answers** (like 15 exam-style questions covering all these traps)? That way you can practice directly.